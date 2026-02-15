"""
AI Assistant Views
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from .openai_helper import AIAssistant
from core.models import Roadmap, Stage, Topic, UserRoadmapEnrollment
from payments.models import UserSubscription, Payment


def has_ai_access(user, roadmap_id=None):
    """
    Check if user has AI access.
    Access granted if:
    1. Active Monthly/Yearly subscription (Global Access)
    2. Enrolled in the specific Premium Roadmap (Contextual Access)
    """
    print(f"DEBUG: Checking AI Access for {user.email}, Roadmap: {roadmap_id}")
    if not user.is_authenticated:
        print("DEBUG: User not authenticated -> False")
        return False

    # 1. Check Global Subscription
    try:
        sub = user.subscription
        allowed_plans = ['monthly', 'yearly', 'quarterly', 'lifetime', 'trial']
        print(f"DEBUG: Sub Status: {sub.status}, Plan: {sub.plan}, End: {sub.end_date}")
        if sub.is_active() and sub.plan and sub.plan.duration_type in allowed_plans:
            print("DEBUG: Global Subscription Active -> True")
            return True
    except UserSubscription.DoesNotExist:
        print("DEBUG: No Subscription Found")
    
    # 2. Check Contextual Access (if roadmap_id provided)
    if roadmap_id:
        try:
            roadmap = Roadmap.objects.get(id=roadmap_id)
            
            # Case A: Free Roadmap
            if not roadmap.is_premium:
                print(f"DEBUG: Roadmap {roadmap_id} is Free -> Access Granted")
                return True
                
            # Case B: Purchased Roadmap
            has_purchase = Payment.objects.filter(
                user=user,
                roadmap=roadmap,
                status='success'
            ).exists()
            
            if has_purchase:
                print(f"DEBUG: Roadmap {roadmap_id} Purchased -> Access Granted")
                return True
                
        except Roadmap.DoesNotExist:
            print(f"DEBUG: Roadmap {roadmap_id} not found")

    print("DEBUG: Access Denied -> False")
    return False


@login_required
def ai_chat_view(request):
    """AI chat interface"""
    
    # Contextual check
    roadmap_id = request.GET.get('roadmap_id')
    
    # Check subscription access
    if not has_ai_access(request.user, roadmap_id):
        from django.contrib import messages
        from django.shortcuts import redirect
        messages.warning(request, 'AI Assistant is a premium feature. Please upgrade to Pro.')
        if roadmap_id:
            return redirect('roadmap_detail', slug=Roadmap.objects.get(id=roadmap_id).slug)
        return redirect('pricing')

    # Get user's enrolled roadmaps for context context
    enrollments = UserRoadmapEnrollment.objects.filter(user=request.user).select_related('roadmap')
    
    context = {
        'enrollments': enrollments,
        'current_roadmap_id': int(roadmap_id) if roadmap_id else None
    }
    return render(request, 'ai/chat.html', context)


@login_required
@require_POST
def ai_ask(request):
    """Handle AI assistant questions"""
    
    try:
        data = json.loads(request.body)
        roadmap_id = data.get('roadmap_id')
        
        # Check access with context
        if not has_ai_access(request.user, roadmap_id):
            return JsonResponse({'error': 'Upgrade to Pro plan to access AI features'}, status=403)
            
        user_message = data.get('message', '')
        
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)
        
        # Get context if provided
        context = {}
        
        stage_id = data.get('stage_id')
        topic_id = data.get('topic_id')
        
        if roadmap_id:
            try:
                roadmap = Roadmap.objects.get(id=roadmap_id)
                context['roadmap'] = roadmap.title
            except Roadmap.DoesNotExist:
                pass
        
        if stage_id:
            try:
                stage = Stage.objects.get(id=stage_id)
                context['stage'] = stage.title
            except Stage.DoesNotExist:
                pass
        
        if topic_id:
            try:
                topic = Topic.objects.get(id=topic_id)
                context['topic'] = topic.title
            except Topic.DoesNotExist:
                pass
        
        # Add user context
        context['user'] = {
            'study_type': request.user.study_type,
            'branch': request.user.branch,
        }
        
        # Get AI response
        ai = AIAssistant()
        response = ai.get_response(user_message, context)
        
        return JsonResponse({
            'response': response,
            'success': True
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
@require_POST
def ai_explain_topic(request, topic_id):
    """Get AI explanation of a topic"""
    
    try:
        topic = Topic.objects.get(id=topic_id)
        
        # Check access (Context: Topic belongs to a Roadmap)
        roadmap_id = topic.stage.roadmap.id
        if not has_ai_access(request.user, roadmap_id):
            return JsonResponse({'error': 'Upgrade to Pro plan to access AI features'}, status=403)
        
        ai = AIAssistant()
        explanation = ai.explain_topic(topic.title, topic.content)
        
        return JsonResponse({
            'explanation': explanation,
            'success': True
        })
    
    except Topic.DoesNotExist:
        return JsonResponse({'error': 'Topic not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
