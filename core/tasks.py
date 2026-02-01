from celery import shared_task
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone
from .models import BroadcastEmail, ProgressEmailCampaign, User, UserRoadmapEnrollment, Topic, UserTopicProgress

@shared_task
def send_broadcast_email_task(broadcast_email_id):
    """
    Background task to send broadcast emails.
    """
    try:
        email_obj = BroadcastEmail.objects.get(id=broadcast_email_id)
    except BroadcastEmail.DoesNotExist:
        return f"BroadcastEmail {broadcast_email_id} not found."
    
    if email_obj.sent_at:
        return f"BroadcastEmail {broadcast_email_id} already sent."

    # Fetch recent users (e.g. 1000 limit for now, or all active)
    # The requirement is "manage 1000+ user", so let's bump the limit or remove it.
    users = User.objects.filter(is_active=True).order_by('-date_joined')
    recipient_list = [user.email for user in users if user.email]
    
    if not recipient_list:
        return "No active users found."

    # Send in batches of 500 to avoid hitting limits or memory issues
    batch_size = 500
    connection = get_connection()
    sent_count = 0
    
    from_email = settings.DEFAULT_FROM_EMAIL or 'noreply@99roadmap.com'
    
    # Render template once
    html_message = render_to_string('emails/broadcast_email.html', {
        'subject': email_obj.subject,
        'message_content': email_obj.message,
        'site_url': settings.SITE_URL
    })

    for i in range(0, len(recipient_list), batch_size):
        batch = recipient_list[i:i + batch_size]
        
        try:
             # Using BCC for privacy
            msg = EmailMultiAlternatives(
                subject=email_obj.subject,
                body=email_obj.message,
                from_email=from_email,
                to=[from_email], 
                bcc=batch,
                connection=connection
            )
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            sent_count += len(batch)
        except Exception as e:
            print(f"Error sending batch {i}: {e}")

    # Update model
    email_obj.sent_at = timezone.now()
    email_obj.recipients_count = sent_count
    email_obj.save()
    
    return f"Sent broadcast to {sent_count} users."

@shared_task
def send_progress_reminder_task(campaign_id):
    """
    Background task to send personalized progress reminders.
    """
    try:
        campaign = ProgressEmailCampaign.objects.get(id=campaign_id)
    except ProgressEmailCampaign.DoesNotExist:
        return f"Campaign {campaign_id} not found."

    if campaign.sent_at:
        return f"Campaign {campaign_id} already sent."

    # Fetch valid users
    users_with_enrollments = User.objects.filter(enrollments__isnull=False).distinct()
    users_with_sub = User.objects.filter(subscription__status='active').distinct()
    target_users = (users_with_enrollments | users_with_sub).distinct()

    if not target_users.exists():
        return "No target users found."

    connection = get_connection()
    messages_to_send = []
    sent_count = 0
    from_email = settings.DEFAULT_FROM_EMAIL or 'noreply@99roadmap.com'

    for user in target_users:
        if not user.email:
            continue
            
        # Gather Data
        enrollments_data = []
        user_enrollments = UserRoadmapEnrollment.objects.filter(user=user).select_related('roadmap')
        
        for enrollment in user_enrollments:
            total_topics = Topic.objects.filter(stage__roadmap=enrollment.roadmap).count()
            completed_topics = UserTopicProgress.objects.filter(
                user=user, 
                topic__stage__roadmap=enrollment.roadmap,
                is_completed=True
            ).count()
            
            enrollments_data.append({
                'roadmap': enrollment.roadmap,
                'percentage': enrollment.get_progress_percentage(),
                'completed_topics': completed_topics,
                'total_topics': total_topics,
                'current_stage_title': enrollment.current_stage.title if enrollment.current_stage else "Not Started"
            })
        
        # Render
        html_body = render_to_string('emails/progress_reminder.html', {
            'user': user,
            'message_content': campaign.intro_message,
            'enrollments': enrollments_data,
            'site_url': settings.SITE_URL,
        })
        
        msg = EmailMultiAlternatives(
            subject=campaign.subject,
            body="Progress Update",
            from_email=from_email,
            to=[user.email],
            connection=connection
        )
        msg.attach_alternative(html_body, "text/html")
        messages_to_send.append(msg)
        
        # Flush batch
        if len(messages_to_send) >= 50:
            connection.send_messages(messages_to_send)
            sent_count += len(messages_to_send)
            messages_to_send = []

    # Final flush
    if messages_to_send:
        connection.send_messages(messages_to_send)
        sent_count += len(messages_to_send)

    campaign.sent_at = timezone.now()
    campaign.recipients_count = sent_count
    campaign.save()

    return f"Sent progress emails to {sent_count} users."
