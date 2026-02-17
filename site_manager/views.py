from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UserSession, GuideCampaign
import json

@csrf_exempt
def track_action(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error'}, status=405)
    
    try:
        data = json.loads(request.body)
        session_key = data.get('session_key')
        event_type = data.get('event_type')
        path = data.get('path')
        
        if not session_key:
            return JsonResponse({'status': 'error'}, status=400)
            
        session, _ = UserSession.objects.get_or_create(session_key=session_key)
        
        if request.user.is_authenticated:
            session.user = request.user
            
        session.last_active = timezone.now()
        
        # Update Page Views
        if event_type == 'page_view':
            views = session.page_views
            views[path] = views.get(path, 0) + 1
            session.page_views = views
            
        # Update Interests
        if path:
            interests = session.interests
            keywords = {
                'python': ['python', 'django'],
                'js': ['javascript', 'react', 'node'],
                'java': ['java', 'spring'],
            }
            for key, terms in keywords.items():
                if any(term in path.lower() for term in terms):
                    interests[key] = interests.get(key, 0) + 1
            session.interests = interests
            
        session.save()
        return JsonResponse({'status': 'success'})
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def get_suggestion(request):
    session_key = request.GET.get('session')
    if not session_key:
        return JsonResponse({'show_message': False})
        
    try:
        session = UserSession.objects.get(session_key=session_key)
        
        # --- Advanced Context Engine ---
        
        # 1. Ready to Buy (High Intent)
        # If user visited plans and features multiple times
        if session.page_views.get('/payments/plans/', 0) > 1:
            return JsonResponse({
                'show_message': True,
                'message': "Ready to level up? 🚀 Get unlimited access to all roadmaps & AI mentor.",
                'actions': [
                    {'label': '⚡ Get Pro (₹499)', 'type': 'link', 'url': '/payments/plans/'}, # Monthly
                    {'label': 'View Plans', 'type': 'link', 'url': '/payments/plans/'}
                ]
            })

        # 2. Python Interest (Specific Roadmap)
        if session.interests.get('python', 0) > 2:
             # Check if already enrolled (mock check for now, real check needs user)
             return JsonResponse({
                'show_message': True,
                'message': "Master Python Backend Development with our curated path! 🐍",
                'actions': [
                    {'label': 'View Roadmap', 'type': 'link', 'url': '/roadmap/python-backend-development/'},
                    {'label': 'Start Quiz', 'type': 'action', 'action': 'quiz', 'data': 'python'}
                ]
            })

        # 3. New User / Explorer
        if len(session.page_views) < 3:
             return JsonResponse({
                'show_message': True,
                'message': "Welcome to 99Roadmap! 👋 Not sure where to start?",
                'actions': [
                    {'label': 'Explore Roadmaps', 'type': 'link', 'url': '/roadmaps/'},
                    {'label': 'Free Trial', 'type': 'link', 'url': '/payments/plans/'}
                ]
            })
            
        return JsonResponse({'show_message': False})
        
    except UserSession.DoesNotExist:
        return JsonResponse({'show_message': False})

@login_required
def enroll_and_redirect(request, roadmap_id):
    """
    Simple synchronous view to enroll user and redirect to dashboard.
    Replaces fragile JS fetch logic.
    """
    roadmap = get_object_or_404(Roadmap, id=roadmap_id, is_active=True)
    
    # Enroll user
    UserRoadmapEnrollment.objects.get_or_create(
        user=request.user,
        roadmap=roadmap
    )
    
    messages.success(request, f"Successfully enrolled in {roadmap.title}! 🚀")
    return redirect('dashboard')

@csrf_exempt
def enroll_from_guide(request):
    """API to enroll user directly from guide"""
    print(f"DEBUG: enroll_from_guide called by {request.user}")
    
    if request.method != 'POST' or not request.user.is_authenticated:
        print("DEBUG: Auth failed or invalid method")
        return JsonResponse({'status': 'error', 'message': 'Login required'}, status=403)
        
    try:
        data = json.loads(request.body)
        roadmap_id = data.get('roadmap_id')
        print(f"DEBUG: Enrollment requested for roadmap {roadmap_id}")
        
        from core.models import Roadmap, UserRoadmapEnrollment
        
        roadmap = Roadmap.objects.get(id=roadmap_id)
        
        # Check if already enrolled
        if UserRoadmapEnrollment.objects.filter(user=request.user, roadmap=roadmap).exists():
             print("DEBUG: Already enrolled")
             return JsonResponse({'status': 'success', 'message': 'Already enrolled'})
             
        # Create enrollment
        UserRoadmapEnrollment.objects.create(user=request.user, roadmap=roadmap)
        print("DEBUG: Enrollment created successfully")
        
        return JsonResponse({'status': 'success', 'message': 'Enrolled successfully!'})
        
    except Roadmap.DoesNotExist:
        print("DEBUG: Roadmap not found")
        return JsonResponse({'status': 'error', 'message': 'Roadmap not found'}, status=404)
    except Exception as e:
        print(f"DEBUG: Error - {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        roadmap_id = data.get('roadmap_id')
        
        # Logic to enroll user (using core.models)
        from core.models import UserRoadmapEnrollment, Roadmap
        
        roadmap = Roadmap.objects.get(id=roadmap_id)
        UserRoadmapEnrollment.objects.get_or_create(user=request.user, roadmap=roadmap)
        
        return JsonResponse({'status': 'success', 'message': f'Enrolled in {roadmap.title}!'})
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def suggest_roadmap(request):
    """API to suggest roadmap based on user input (Dynamic & DB-Driven)"""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
        
    try:
        data = json.loads(request.body)
        level = data.get('level', 'beginner').lower()
        goal_input = data.get('goal', '').lower().strip()
        
        from core.models import Roadmap
        from django.db.models import Q
        
        # 1. Improved Token-Based Search Logic
        import re
        
        # Normalize input: lowercase, remove special chars
        clean_input = re.sub(r'[^a-zA-Z0-9\s]', '', goal_input)
        tokens = clean_input.split()
        
        # Stop words to filter out noise
        stop_words = {'i', 'want', 'to', 'learn', 'become', 'a', 'an', 'the', 'roadmap', 'course', 'developer', 'engineer', 'expert', 'master', 'begin', 'start', 'coding', 'programming', 'career', 'job', 'in', 'with', 'for', 'about'}
        
        search_terms = [t for t in tokens if t not in stop_words and len(t) > 1]
        
        # If we have specific known tech keywords in the input, prioritize them
        base_tech_keywords = ['python', 'java', 'javascript', 'react', 'node', 'django', 'spring', 'go', 'golang', 'rust', 'c++', 'c#', 'php', 'ruby', 'swift', 'kotlin', 'flutter', 'aws', 'docker', 'kubernetes', 'linux', 'sql', 'mysql', 'postgres', 'mongo', 'html', 'css', 'frontend', 'backend', 'fullstack', 'ai', 'ml', 'data', 'cloud', 'devops', 'mobile', 'game', 'security', 'cyber', 'blockchain', 'web3']
        
        priority_keywords = [t for t in tokens if t in base_tech_keywords]
        
        # Use priority keywords if available, otherwise use all significant search terms
        final_keywords = priority_keywords if priority_keywords else search_terms
        
        # 2. Build Query
        # Difficulty Match
        diff_q = Q(difficulty__iexact=level)
        if level == 'intermediate':
            diff_q |= Q(difficulty='advanced') # Allow slightly harder

        # Keyword Match
        keyword_q = Q()
        if final_keywords:
            for kw in final_keywords:
                # Search in Title (High weight) or Description (Lower weight)
                keyword_q |= Q(title__icontains=kw) | Q(description__icontains=kw)

        # 3. Fetch & Rank Results
        matches = Roadmap.objects.none()
        reason = ""

        # Strategy A: Strict Match (Level + Keywords)
        if final_keywords:
            matches = Roadmap.objects.filter(is_active=True).filter(diff_q & keyword_q).order_by('-enrolled_count')
            if matches.exists():
                matched_term = final_keywords[0].title()
                reason = f"Perfect match for '{matched_term}' at {level} level!"
        
        # Strategy B: Keywords Only (Ignore Level)
        if not matches.exists() and final_keywords:
            matches = Roadmap.objects.filter(is_active=True).filter(keyword_q).order_by('-enrolled_count')
            if matches.exists():
                reason = f"Found a great roadmap for '{final_keywords[0].title()}'."

        # Strategy C: Fuzzy / Broad Match (if no exact keywords found)
        # If user typed something we couldn't parse well, just try the raw input as a broad search
        if not matches.exists() and len(goal_input) > 3:
             broad_q = Q(title__icontains=goal_input) | Q(description__icontains=goal_input)
             matches = Roadmap.objects.filter(is_active=True).filter(broad_q).order_by('-enrolled_count')
             if matches.exists():
                 reason = f"This looks relevant to '{goal_input}'."

        # Strategy D: Level Only (Popularity Fallback)
        if not matches.exists():
            matches = Roadmap.objects.filter(is_active=True).filter(diff_q).order_by('-enrolled_count')
            if matches.exists():
                reason = f"We couldn't find an exact match for '{goal_input}', but this is our top {level} roadmap!"

        # Strategy D: Absolute Fallback (Most Popular Overall)
        if not matches.exists():
             matches = Roadmap.objects.filter(is_active=True).order_by('-enrolled_count')
             reason = "Our most popular roadmap to get you started!"
             
        best_match = matches.first()
        
        if not best_match:
             return JsonResponse({'status': 'error', 'message': 'No roadmaps available.'}, status=404)

        return JsonResponse({
            'status': 'success',
            'roadmap': {
                'id': best_match.id,
                'title': best_match.title,
                'slug': best_match.slug,
                'description': best_match.description[:120] + '...',
                'image': best_match.thumbnail.url if best_match.thumbnail else '/static/images/default-roadmap.png',
                'enrolled': best_match.enrolled_count,
                'rating': '4.9' # Placeholder
            },
            'reason': reason
        })
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
