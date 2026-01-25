"""
Views for 99Roadmap Platform
Handles authentication, roadmaps, progress, and user interactions
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count, Avg
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.urls import reverse
import uuid
import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color

from .models import (
    User, UserGamification, Roadmap, RoadmapCategory, Stage, Topic, Quiz,
    QuizQuestion, QuizOption, UserRoadmapEnrollment, UserTopicProgress,
    UserQuizAttempt, XPTransaction
)
from payments.models import UserSubscription, Payment
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserAvatarForm, QuizSubmissionForm


# ==================== Authentication Views ====================

def register_view(request):
    """User registration - no email verification required"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_verified = True  # Auto-verify users
            user.save()
            
            # Create gamification profile
            UserGamification.objects.create(user=user)
            
            # Send Welcome Email
            try:
                from django.template.loader import render_to_string
                
                html_message = render_to_string('emails/welcome.html', {
                    'user': user,
                    'site_url': settings.SITE_URL
                })
                
                send_mail(
                    subject='Welcome to 99Roadmap! 🚀',
                    message=f"Hi {user.first_name or user.username}, Welcome to 99Roadmap!", # Plain text fallback
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=True,
                    html_message=html_message
                )
            except Exception as e:
                print(f"Error sending welcome email: {e}")
            
            # Auto-login and redirect
            login(request, user)
            messages.success(request, f'Registration successful! Welcome to 99Roadmap.')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'auth/register.html', {'form': form})


def forgot_password_view(request):
    """Forgot password - request reset"""
    
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone', '').strip()
        
        try:
            # Find user by email or phone
            if '@' in email_or_phone:
                user = User.objects.get(email=email_or_phone)
            else:
                user = User.objects.get(phone=email_or_phone)
            
            # Generate reset token
            reset_token = str(uuid.uuid4())
            user.verification_token = reset_token  # Reuse this field for password reset
            user.save()
            
            # Send reset email (or show token if email not configured)
            try:
                from django.template.loader import render_to_string
                
                reset_url = f"{settings.SITE_URL}{reverse('reset_password', args=[reset_token])}"
                html_message = render_to_string('emails/reset_password.html', {
                    'user': user,
                    'reset_url': reset_url,
                    'site_url': settings.SITE_URL
                })
                
                send_mail(
                    subject='Reset Your Password - 99Roadmap',
                    message=f'Reset your password: {reset_url}', # Plain text fallback
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                    html_message=html_message
                )
                messages.success(request, f'Password reset link sent to {user.email}. Please check your email.')
            except Exception as e:
                # If email fails, show the reset link directly
                reset_url = reverse('reset_password', args=[reset_token])
                messages.success(request, f'Click here to reset password: <a href="{reset_url}">Reset Password</a> (Email not configured)')
            
            return redirect('login')
            
        except User.DoesNotExist:
            messages.error(request, 'No account found with that email or phone number.')
    
    return render(request, 'auth/forgot_password.html')


def reset_password_view(request, token):
    """Reset password with token"""
    
    try:
        user = User.objects.get(verification_token=token)
    except User.DoesNotExist:
        messages.error(request, 'Invalid or expired reset link.')
        return redirect('login')
    
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
        else:
            user.set_password(password1)
            user.verification_token = ''  # Clear the token
            user.save()
            messages.success(request, 'Password reset successful! You can now login.')
            return redirect('login')
    
    return render(request, 'auth/reset_password.html', {'token': token})


def login_view(request):
    """User login - accepts email or phone"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            # Authentication handled by UserLoginForm.clean()
            user = form.get_user()
            
            if user is not None:
                login(request, user)
                
                # Update streak
                try:
                    gamification = user.gamification
                    gamification.update_streak()
                except UserGamification.DoesNotExist:
                    UserGamification.objects.create(user=user)
                
                messages.success(request, f'Welcome back, {user.get_short_name()}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email/phone or password.')
        else:
            messages.error(request, 'Invalid email/phone or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'auth/login.html', {'form': form})



@login_required
def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_view(request):
    """User profile and settings"""
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update_avatar':
            avatar_form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
            if avatar_form.is_valid():
                avatar_form.save()
                messages.success(request, 'Profile picture updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Error updating profile picture.')
                
        elif action == 'update_profile':
            form = UserProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')
    
    # Initialize forms
    form = UserProfileForm(instance=request.user)
    # We don't really need to pass avatar_form to template if we use manual input, 
    # but good for consistency if needed. Be careful not to overwrite 'form' data on GET.
    
    try:
        gamification = request.user.gamification
    except UserGamification.DoesNotExist:
        gamification = UserGamification.objects.create(user=request.user)
    
    enrollments = UserRoadmapEnrollment.objects.filter(user=request.user)
    
    # Calculate Profile Setup Progress (KYC)
    # Step 1: Register (Always done if logged in) - 33%
    # Step 2: Socials (LinkedIn or GitHub) - 66%
    # Step 3: Goals - 100%
    
    current_step = 1
    progress_percentage = 33
    
    has_socials = bool(request.user.linkedin_profile or request.user.github_profile)
    has_goals = bool(request.user.future_goals)
    
    if has_goals:
        current_step = 4 # Completed
        progress_percentage = 100
    elif has_socials:
        current_step = 3
        progress_percentage = 66
    else:
        current_step = 2

    # Steps for UI
    setup_steps = [
        {'step': 1, 'title': 'Register', 'is_completed': True},
        {'step': 2, 'title': 'Connect Socials', 'is_completed': has_socials},
        {'step': 3, 'title': 'Set Goals', 'is_completed': has_goals},
    ]

    # Purchase Stats
    stats = {
        'roadmaps_count': UserRoadmapEnrollment.objects.filter(user=request.user).count(),
        'bundles_count': Payment.objects.filter(user=request.user, bundle__isnull=False, status='success').count(),
        'subscriptions_count': Payment.objects.filter(user=request.user, subscription_plan__isnull=False, status='success').count(),
    }
    
    # Detailed lists for Modals
    purchased_bundles = Payment.objects.filter(
        user=request.user, 
        bundle__isnull=False, 
        status='success'
    ).select_related('bundle').order_by('-created_at')
    
    subscription_history = Payment.objects.filter(
        user=request.user, 
        subscription_plan__isnull=False, 
        status='success'
    ).select_related('subscription_plan').order_by('-created_at')

    context = {
        'form': form,
        'gamification': gamification,
        'enrollments': enrollments,
        'setup_steps': setup_steps,
        'current_step': current_step,
        'progress_percentage': progress_percentage,
        'stats': stats,
        'purchased_bundles': purchased_bundles,
        'subscription_history': subscription_history,
    }
    return render(request, 'profile/profile.html', context)


# ==================== Home & Dashboard ====================

def home_view(request):
    """Landing page"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    featured_roadmaps = Roadmap.objects.filter(is_active=True, is_featured=True)[:6]
    categories = RoadmapCategory.objects.all()[:6]
    all_roadmaps = Roadmap.objects.filter(is_active=True).select_related('category')
    
    context = {
        'featured_roadmaps': featured_roadmaps,
        'categories': categories,
        'all_roadmaps': all_roadmaps,
    }
    return render(request, 'home.html', context)


@login_required
def dashboard_view(request):
    """User dashboard with personalized content"""
    
    try:
        gamification = request.user.gamification
    except UserGamification.DoesNotExist:
        gamification = UserGamification.objects.create(user=request.user)
    
    # Get user's enrollments
    enrollments = UserRoadmapEnrollment.objects.filter(user=request.user).select_related('roadmap', 'current_stage')
    
    # Get recent activity
    recent_topics_qs = UserTopicProgress.objects.filter(user=request.user, is_completed=True).order_by('-completed_at')
    recent_quizzes_qs = UserQuizAttempt.objects.filter(user=request.user).order_by('-started_at')
    
    recent_topics = recent_topics_qs[:5]
    recent_quizzes = recent_quizzes_qs[:5]
    
    # Get recommended roadmaps
    recommended = Roadmap.objects.filter(is_active=True).exclude(
        id__in=enrollments.values_list('roadmap_id', flat=True)
    )[:3]

    # --- Enhanced Dashboard Data ---
    
    # 1. Skill Stats (Dynamic based on completed topics by category)
    # Get all categories
    categories = RoadmapCategory.objects.all()
    skill_list = []
    
    for cat in categories:
        # Get total topics in this category
        total_topics = Topic.objects.filter(stage__roadmap__category=cat).count()
        if total_topics > 0:
            # Get completed topics by user in this category
            completed = UserTopicProgress.objects.filter(
                user=request.user, 
                is_completed=True,
                topic__stage__roadmap__category=cat
            ).count()
            
            percentage = int((completed / total_topics) * 100)
            skill_list.append({
                'label': cat.name,
                'percentage': percentage
            })
    
    # Fallback if no data
    if not skill_list:
        skill_list.append({'label': 'No Data', 'percentage': 0})
    
    # 2. Daily Goals (Dynamic)
    today = timezone.now().date()
    
    # Check actual progress
    has_login = True # User is here
    topics_today = recent_topics_qs.filter(completed_at__date=today).count()
    quizzes_today = recent_quizzes_qs.filter(created_at__date=today).count() if hasattr(UserQuizAttempt, 'created_at') else recent_quizzes_qs.filter(completed_at__date=today).count()
    # Note: UserQuizAttempt uses 'completed_at' usually, check model. Using started_at/completed_at.
    # In view above: UserQuizAttempt... order_by('-started_at'), and create uses 'completed_at'.
    quizzes_today_count = UserQuizAttempt.objects.filter(user=request.user, completed_at__date=today).count()

    daily_goals = [
        {'title': 'Login to Platform', 'completed': True, 'xp': 10},
        {'title': 'Complete 1 Topic', 'completed': topics_today >= 1, 'xp': 50},
        {'title': 'Pass 1 Quiz', 'completed': quizzes_today_count >= 1, 'xp': 100},
    ]
    
    daily_completed_count = sum(1 for g in daily_goals if g['completed'])
    daily_progress_percent = int((daily_completed_count / len(daily_goals)) * 100)
    
    # 3. Leaderboard Top 3
    leaderboard_top = UserGamification.objects.select_related('user').order_by('-total_xp')[:3]
    
    # 4. Badges (Mock or fetch if model exists)
    badges = [
        {'name': 'Early Adopter', 'icon': 'fas fa-rocket', 'color': 'text-primary'},
        {'name': 'Fast Learner', 'icon': 'fas fa-bolt', 'color': 'text-warning'},
    ]

    context = {
        'gamification': gamification,
        'enrollments': enrollments,
        'recent_topics': recent_topics,
        'recent_quizzes': recent_quizzes,
        'recommended': recommended,
        # New Enchanced Data
        'skill_list': skill_list,
        'daily_goals': daily_goals,
        'daily_completed_count': daily_completed_count,
        'daily_total_count': len(daily_goals),
        'daily_progress_percent': daily_progress_percent,
        'leaderboard_top': leaderboard_top,
        'badges': badges,
    }
    return render(request, 'dashboard.html', context)


# ==================== Roadmap Views ====================

def roadmap_list_view(request):
    """List all roadmaps with filtering"""
    
    roadmaps = Roadmap.objects.filter(is_active=True)
    categories = RoadmapCategory.objects.all()
    
    # Filtering
    category_slug = request.GET.get('category')
    difficulty = request.GET.get('difficulty')
    search = request.GET.get('search')
    
    if category_slug:
        roadmaps = roadmaps.filter(category__slug=category_slug)
    
    if difficulty:
        roadmaps = roadmaps.filter(difficulty=difficulty)
    
    if search:
        roadmaps = roadmaps.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(roadmaps, 12)
    page = request.GET.get('page')
    roadmaps_page = paginator.get_page(page)
    
    context = {
        'roadmaps': roadmaps_page,
        'categories': categories,
        'selected_category': category_slug,
        'selected_difficulty': difficulty,
        'search_query': search,
    }
    return render(request, 'roadmaps/list.html', context)


def roadmap_detail_view(request, slug):
    """Roadmap detail page"""
    
    roadmap = get_object_or_404(Roadmap, slug=slug, is_active=True)
    stages = roadmap.stages.all().prefetch_related('topics', 'quizzes')
    
    enrollment = None
    user_has_access = False
    
    if request.user.is_authenticated:
        enrollment, created = UserRoadmapEnrollment.objects.get_or_create(
            user=request.user,
            roadmap=roadmap
        )
        
        # Check if user has access (subscribed or free content)
        if not roadmap.is_premium:
            user_has_access = True
        else:
            # Check subscription (will implement in payments app)
            has_subscription = getattr(request.user, 'has_active_subscription', lambda: False)()
            
            # Check for direct purchase
            has_purchase = Payment.objects.filter(
                user=request.user,
                roadmap=roadmap,
                status='success'
            ).exists()
            
            user_has_access = has_subscription or has_purchase
    
    context = {
        'roadmap': roadmap,
        'stages': stages,
        'enrollment': enrollment,
        'user_has_access': user_has_access,
    }
    return render(request, 'roadmaps/detail.html', context)


@login_required
def stage_detail_view(request, roadmap_slug, stage_order):
    """Stage detail with topics"""
    
    roadmap = get_object_or_404(Roadmap, slug=roadmap_slug, is_active=True)
    stage = get_object_or_404(Stage, roadmap=roadmap, order=stage_order)
    
    # Check access
    user_has_access = not roadmap.is_premium or stage.is_free
    
    if not user_has_access:
        # Check subscription
        user_has_access = getattr(request.user, 'has_active_subscription', lambda: False)()
    
    if not user_has_access:
        messages.warning(request, 'This stage requires a subscription. Please subscribe to continue.')
        return redirect('roadmap_detail', slug=roadmap_slug)
    
    topics = stage.topics.all()
    quizzes = stage.quizzes.all()
    
    # Get user progress
    completed_topics = UserTopicProgress.objects.filter(
        user=request.user,
        topic__in=topics,
        is_completed=True
    ).values_list('topic_id', flat=True)

    # Check AI access
    # Local import to avoid circular dependency if any (though ai_assistant views import core models)
    from ai_assistant.views import has_ai_access
    is_ai_locked = not has_ai_access(request.user, roadmap.id)
    print(f"DEBUG: Stage View - User: {request.user}, Roadmap: {roadmap.id}, Locked: {is_ai_locked}")
    
    context = {
        'roadmap': roadmap,
        'stage': stage,
        'topics': topics,
        'quizzes': quizzes,
        'completed_topics': list(completed_topics),
        'is_ai_locked': is_ai_locked,
    }
    return render(request, 'roadmaps/stage.html', context)


@login_required
def topic_view(request, topic_id):
    """View topic content"""
    # Local import to avoid circular dependency
    from ai_assistant.views import has_ai_access
    
    topic = get_object_or_404(Topic, id=topic_id)
    stage = topic.stage
    roadmap = stage.roadmap
    
    # Check access
    user_has_access = not roadmap.is_premium or stage.is_free
    if not user_has_access:
        user_has_access = getattr(request.user, 'has_active_subscription', lambda: False)()
    
    if not user_has_access:
        messages.warning(request, 'You need a subscription to access this content.')
        return redirect('roadmap_detail', slug=roadmap.slug)
    
    # Get or create progress
    progress, created = UserTopicProgress.objects.get_or_create(
        user=request.user,
        topic=topic
    )
    
    # Get next and previous topics
    next_topic = Topic.objects.filter(stage=stage, order__gt=topic.order).first()
    prev_topic = Topic.objects.filter(stage=stage, order__lt=topic.order).last()
    
    # Check AI access
    is_ai_locked = not has_ai_access(request.user, roadmap.id)
    print(f"DEBUG: Topic View - User: {request.user}, Roadmap: {roadmap.id}, Locked: {is_ai_locked}")
    
    context = {
        'topic': topic,
        'stage': stage,
        'roadmap': roadmap,
        'progress': progress,
        'next_topic': next_topic,
        'prev_topic': prev_topic,
        'is_ai_locked': is_ai_locked,
    }
    return render(request, 'roadmaps/topic.html', context)


@login_required
@require_POST
def mark_topic_complete(request, topic_id):
    """Mark topic as completed and award XP"""
    
    topic = get_object_or_404(Topic, id=topic_id)
    
    progress, created = UserTopicProgress.objects.get_or_create(
        user=request.user,
        topic=topic
    )
    
    if not progress.is_completed:
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.save()
        
        # Award XP
        try:
            gamification = request.user.gamification
            gamification.add_xp(topic.xp_reward)
            gamification.topics_completed += 1
            gamification.save()
            
            # Log transaction
            XPTransaction.objects.create(
                user=request.user,
                amount=topic.xp_reward,
                action='topic_complete',
                description=f'Completed: {topic.title}'
            )
            
            return JsonResponse({'success': True, 'xp_earned': topic.xp_reward})
        except UserGamification.DoesNotExist:
            UserGamification.objects.create(user=request.user)
            return JsonResponse({'success': True})
    
    return JsonResponse({'success': True, 'already_completed': True})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count, Avg
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
import uuid

from .models import (
    User, UserGamification, Roadmap, RoadmapCategory, Stage, Topic, Quiz,
    QuizQuestion, QuizOption, UserRoadmapEnrollment, UserTopicProgress,
    UserQuizAttempt, XPTransaction
)
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, QuizSubmissionForm
from ai_assistant.openai_helper import AIAssistant


# ... [Existing Authentication Views Code Omitted for Brevity - Keeping Imports] ...
# To ensure context, I'm replacing from line 446 onwards (the Quiz Views section)
# But wait, I can't partially match easily. I'll target the Quiz Views section specifically.


# ==================== Quiz Views ====================

@login_required
def quiz_view(request, quiz_id=None, stage_id=None):
    """
    Take a quiz.
    If quiz_id is provided, takes that specific quiz.
    If stage_id is provided, takes the quiz for that stage, generating one if needed.
    """
    
    quiz = None
    
    if quiz_id:
        quiz = get_object_or_404(Quiz, id=quiz_id)
        stage = quiz.stage
    elif stage_id:
        stage = get_object_or_404(Stage, id=stage_id)
        # Try to find existing required quiz
        quiz = stage.quizzes.filter(is_required=True).first()
        
        # If no quiz exists, GENERATE one using AI
        if not quiz:
            try:
                ai = AIAssistant()
                topics = stage.topics.all()
                topic_summaries = [f"{t.title}: {t.content[:200]}" for t in topics]
                
                quiz_data = ai.generate_quiz_for_stage(stage.title, topic_summaries)
                
                if quiz_data:
                    # Create Quiz
                    quiz = Quiz.objects.create(
                        stage=stage,
                        title=f"{stage.title} - Final Assessment",
                        description=f"Auto-generated assessment for {stage.title}",
                        is_required=True,
                        xp_reward=100
                    )
                    
                    # Create Questions
                    for idx, q_data in enumerate(quiz_data, 1):
                        question = QuizQuestion.objects.create(
                            quiz=quiz,
                            question_text=q_data['question'],
                            question_type='single', # AI returns multiple choice which maps to 'single' selection usually
                            explanation=q_data.get('explanation', ''),
                            order=idx
                        )
                        
                        # Create Options
                        correct_idx = q_data.get('correct_index', 0)
                        for opt_idx, opt_text in enumerate(q_data['options']):
                            QuizOption.objects.create(
                                question=question,
                                option_text=opt_text,
                                is_correct=(opt_idx == correct_idx),
                                order=opt_idx + 1
                            )
            except Exception as e:
                print(f"Error generating quiz: {e}")
                messages.error(request, "Unable to generate quiz at this time. Please try again later.")
                return redirect('roadmap_detail', slug=stage.roadmap.slug)
    
    if not quiz:
        messages.warning(request, "No quiz available for this stage.")
        return redirect('roadmap_detail', slug=stage.roadmap.slug)

    stage = quiz.stage
    roadmap = stage.roadmap
    
    # Check access
    user_has_access = not roadmap.is_premium or stage.is_free
    if not user_has_access:
        user_has_access = getattr(request.user, 'has_active_subscription', lambda: False)()
    
    if not user_has_access:
        messages.warning(request, 'You need a subscription to take this quiz.')
        return redirect('roadmap_detail', slug=roadmap.slug)
    
    
    # Check if all topics in the stage are completed
    total_topics = stage.topics.count()
    completed_topics = UserTopicProgress.objects.filter(
        user=request.user,
        topic__stage=stage,
        is_completed=True
    ).count()
    
    if completed_topics < total_topics:
        messages.warning(request, f'You must complete all {total_topics} topics in this stage before taking the quiz.')
        return redirect('stage_detail', roadmap_slug=roadmap.slug, stage_order=stage.order)

    if request.method == 'POST':
        form = QuizSubmissionForm(quiz, request.POST)
        if form.is_valid():
            # Calculate score
            total_questions = quiz.questions.count()
            if total_questions == 0:
                score = 100 # Fallback
            else:
                correct_answers = 0
                answers = {}
                
                for question in quiz.questions.all():
                    field_name = f'question_{question.id}'
                    user_answer = form.cleaned_data.get(field_name)
                    
                    if question.question_type == 'single':
                        correct_option = question.options.filter(is_correct=True).first()
                        if correct_option and str(correct_option.id) == user_answer:
                            correct_answers += 1
                        answers[question.id] = user_answer
                    
                    elif question.question_type == 'multiple':
                        correct_options = set(question.options.filter(is_correct=True).values_list('id', flat=True))
                        user_options = set(int(uid) for uid in user_answer)
                        if correct_options == user_options:
                            correct_answers += 1
                        answers[question.id] = list(user_answer)
                    
                    elif question.question_type == 'truefalse':
                        correct_option = question.options.filter(is_correct=True).first()
                        if correct_option and correct_option.option_text.lower() == user_answer.lower():
                            correct_answers += 1
                        answers[question.id] = user_answer
                
                score = int((correct_answers / total_questions) * 100)
            
            passed = score >= quiz.passing_score
            
            # Save attempt
            attempt = UserQuizAttempt.objects.create(
                user=request.user,
                quiz=quiz,
                score=score,
                passed=passed,
                answers=answers,
                completed_at=timezone.now()
            )
            
            # Award XP & Handle Progression if passed
            if passed:
                try:
                    gamification = request.user.gamification
                    # Only award XP for first pass? For now, award every time or maybe check previous attempts
                    # Simple version: award every time
                    gamification.add_xp(quiz.xp_reward)
                    gamification.quizzes_passed += 1
                    gamification.save()
                    
                    XPTransaction.objects.create(
                        user=request.user,
                        amount=quiz.xp_reward,
                        action='quiz_pass',
                        description=f'Passed: {quiz.title}'
                    )
                    
                    # --- STAGE PROGRESSION LOGIC ---
                    if quiz.is_required:
                        # Mark stage as complete in enrollment
                        enrollment, _ = UserRoadmapEnrollment.objects.get_or_create(
                            user=request.user,
                            roadmap=roadmap
                        )
                        
                        # Find next stage
                        next_stage = Stage.objects.filter(
                            roadmap=roadmap,
                            order__gt=stage.order
                        ).order_by('order').first()
                        
                        if next_stage:
                            enrollment.current_stage = next_stage
                            enrollment.save()
                            messages.success(request, f"Congratulations! You've unlocked the next stage: {next_stage.title}")
                        else:
                            # Roadmap Complete!
                            enrollment.completed_at = timezone.now()
                            enrollment.save()
                            messages.success(request, f"Congratulations! You've completed the {roadmap.title} roadmap!")
                            
                            gamification.roadmaps_completed += 1
                            gamification.save()

                except UserGamification.DoesNotExist:
                    UserGamification.objects.create(user=request.user)
            
            return redirect('quiz_result', attempt_id=attempt.id)
    else:
        form = QuizSubmissionForm(quiz)
    
    context = {
        'quiz': quiz,
        'stage': stage,
        'roadmap': roadmap,
        'form': form,
    }
    return render(request, 'roadmaps/quiz.html', context)


@login_required
def quiz_result_view(request, attempt_id):
    """Show quiz results"""
    
    attempt = get_object_or_404(UserQuizAttempt, id=attempt_id, user=request.user)
    next_stage = None
    
    if attempt.passed and attempt.quiz.is_required:
         next_stage = Stage.objects.filter(
            roadmap=attempt.quiz.stage.roadmap,
            order__gt=attempt.quiz.stage.order
        ).order_by('order').first()

    context = {
        'attempt': attempt,
        'quiz': attempt.quiz,
        'next_stage': next_stage
    }
    return render(request, 'roadmaps/quiz_result.html', context)


# ==================== Leaderboard Views ====================

def leaderboard_view(request):
    """Global XP Leaderboard"""
    
    # Get top 50 users by XP
    top_users = UserGamification.objects.select_related('user').order_by('-total_xp')[:50]
    
    # Find current user's rank if logged in
    user_rank = None
    if request.user.is_authenticated:
        try:
            # This is a bit expensive for large tables but fine for MVP
            # A more efficient way would be using Window functions or raw SQL for rank
            # For now, we'll check if they are in top 50, otherwise query count
            user_gamification = request.user.gamification
            
            # Simple rank calculation: count users with more XP + 1
            rank = UserGamification.objects.filter(total_xp__gt=user_gamification.total_xp).count() + 1
            user_rank = {
                'rank': rank,
                'gamification': user_gamification
            }
        except UserGamification.DoesNotExist:
            pass
            
    context = {
        'top_users': top_users,
        'user_rank': user_rank
    }
    return render(request, 'leaderboard.html', context)


# ==================== PDF Views ====================

@login_required
def download_roadmap_pdf(request, roadmap_id):
    roadmap = get_object_or_404(Roadmap, id=roadmap_id)
    
    # Check if user has initialized payment or if roadmap is free? 
    # Logic: User must be enrolled to download? Or just logged in?
    # Requirement says "add a floating download pdf button". 
    # Usually requires premium access for premium roadmaps.
    
    # Simple check: If premium, user must have enrollment or subscription
    if roadmap.is_premium:
        has_access = False
        if request.user.enrollments.filter(roadmap=roadmap).exists():
            has_access = True
        elif hasattr(request.user, 'subscription') and request.user.subscription.is_active():
            has_access = True
            
        if not has_access:
            messages.error(request, "You need full access to download resources.")
            return redirect('roadmap_detail', slug=roadmap.slug)

    if not roadmap.pdf_file:
         messages.error(request, "No PDF available for this roadmap.")
         return redirect('roadmap_detail', slug=roadmap.slug)

    try:
        # Open the original PDF
        input_pdf = PdfReader(roadmap.pdf_file.path)
        output_pdf = PdfWriter()

        # Create watermark
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Watermark settings
        text = "99Roadmap"
        can.setFont("Helvetica-Bold", 60)
        can.setFillColor(Color(0.5, 0.5, 0.5, 0.2)) # Grey, 20% opacity
        
        # Add watermark diagonally across the page
        can.saveState()
        can.translate(300, 400)
        can.rotate(45)
        can.drawCentredString(0, 0, text)
        can.restoreState()
        
        can.save()
        packet.seek(0)
        
        watermark = PdfReader(packet)
        watermark_page = watermark.pages[0]

        # Apply watermark to each page
        for page in input_pdf.pages:
            page.merge_page(watermark_page)
            output_pdf.add_page(page)

        # Return response
        pdf_buffer = io.BytesIO()
        output_pdf.write(pdf_buffer)
        pdf_buffer.seek(0)
        
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{roadmap.slug}_99roadmap.pdf"'
        return response
        
    except Exception as e:
        print(f"PDF Error: {e}")
        messages.error(request, "Error generating PDF.")
        return redirect('roadmap_detail', slug=roadmap.slug)
# Add these new view functions at the end of core/views.py

# ==================== Static Pages ====================

def contact_view(request):
    """Contact us page"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()
        
        if name and email and subject and message_text:
            try:
                # Send email to admin
                send_mail(
                    subject=f'Contact Form: {subject}',
                    message=f'From: {name} ({email})\n\n{message_text}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'static_pages/contact.html')


def faq_view(request):
    """FAQ page"""
    return render(request, 'static_pages/faq.html')


def terms_view(request):
    """Terms and conditions page"""
    return render(request, 'static_pages/terms.html')


def privacy_view(request):
    """Privacy policy page"""
    return render(request, 'static_pages/privacy.html')


def refund_policy_view(request):
    """Refund policy page"""
    return render(request, 'static_pages/refund_policy.html')
