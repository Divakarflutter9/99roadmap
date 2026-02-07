from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    """
    Send welcome email with coupon code
    """
    try:
        subject = "🎉 You are a Lucky Winner! 50% OFF Inside"
        from_email = settings.DEFAULT_FROM_EMAIL
        to = user.email
        
        context = {
            'user': user,
            'site_url': settings.SITE_URL,
        }
        
        html_content = render_to_string('emails/welcome_coupon.html', context)
        text_content = "Congratulations! You are a lucky winner. Use code LUCKY50 for 50% off."
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print(f"Welcome email sent to {to}")
    except Exception as e:
        print(f"Failed to send welcome email: {e}")

@receiver(user_signed_up)
def populate_profile(request, user, **kwargs):
    """
    Populate user profile from social account data on signup
    """
    # Check if this is a social signup
    if 'sociallogin' in kwargs:
        sociallogin = kwargs['sociallogin']
        
        # Only proceed for Google for now (or make generic)
        if sociallogin.account.provider == 'google':
            data = sociallogin.account.extra_data
            print(f"DEBUG: Google Data: {data}")
            
            # 1. Full Name
            if not user.full_name:
                user.full_name = data.get('name', '')
                if not user.full_name:
                    # Fallback to first/last name
                    first = data.get('given_name', '')
                    last = data.get('family_name', '')
                    user.full_name = f"{first} {last}".strip()
            
            # 2. Email Verification (Google emails are verified)
            if data.get('email_verified', False):
                user.is_verified = True
                
            user.save()
