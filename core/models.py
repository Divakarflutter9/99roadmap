"""
Core Models for 99Roadmap Platform
Includes: User, Roadmap, Stage, Topic, Quiz, Progress
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core.validators import MinValueValidator
import uuid


class UserManager(BaseUserManager):
    """Custom user manager for email-based authentication"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model with extended profile fields"""
    
    STUDY_CHOICES = [
        ('btech', 'B.Tech'),
        ('degree', 'Degree'),
        ('diploma', 'Diploma'),
        ('mtech', 'M.Tech'),
        ('mba', 'MBA'),
        ('other', 'Other'),
    ]
    
    username = None  # Remove username field
    email = models.EmailField('Email Address', unique=True)
    full_name = models.CharField('Full Name', max_length=150)
    phone = models.CharField('Phone Number', max_length=15, blank=True, null=True, unique=True)
    
    # Academic info
    study_type = models.CharField('Study Type', max_length=20, choices=STUDY_CHOICES, default='btech')
    branch = models.CharField('Branch/Department', max_length=100, blank=True)
    year = models.PositiveIntegerField('Year of Study', null=True, blank=True)
    college = models.CharField('College/University', max_length=200, blank=True)
    
    # Verification
    is_verified = models.BooleanField('Email Verified', default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    
    # Profile
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField('Bio', max_length=500, blank=True)
    
    # Socials & Goals
    linkedin_profile = models.URLField('LinkedIn Profile', blank=True)
    github_profile = models.URLField('GitHub Profile', blank=True)
    future_goals = models.TextField('Future Goals', help_text="What are your career aspirations?", blank=True)
    
    # Timestamps
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    objects = UserManager()
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.full_name or self.email
    
    def get_full_name(self):
        return self.full_name
    
    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else ''


class RoadmapCategory(models.Model):
    """Categories for organizing roadmaps"""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='fa-route')  # FontAwesome icon
    color = models.CharField(max_length=20, default='#6366f1')  # Hex color
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Roadmap(models.Model):
    """Learning roadmap containing stages and topics"""
    
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    
    category = models.ForeignKey(RoadmapCategory, on_delete=models.SET_NULL, null=True, related_name='roadmaps')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    
    # Visual
    thumbnail = models.ImageField(upload_to='roadmaps/', null=True, blank=True)
    banner = models.ImageField(upload_to='roadmaps/banners/', null=True, blank=True)
    
    # Pricing
    is_premium = models.BooleanField('Requires Subscription', default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    
    # Resources
    pdf_file = models.FileField(upload_to='roadmaps/pdfs/', null=True, blank=True, help_text='Upload PDF resource for this roadmap')
    
    # Stats
    total_stages = models.PositiveIntegerField(default=0)
    estimated_hours = models.PositiveIntegerField('Estimated Hours', default=0)
    enrolled_count = models.PositiveIntegerField(default=0)
    
    # Metadata
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
    
    def __str__(self):
        return self.title
    
    def update_premium_status(self):
        """
        Update is_premium status based on stages.
        If ALL stages are free, the roadmap is free.
        If ANY stage is not free, the roadmap is premium.
        """
        # If there are no stages, default to current setting or True/False depending on logic, 
        # but let's say if no stages, it follows the manual setting. 
        # However, the requirement is "if all stages are free -> free".
        if self.stages.exists():
            # Check if there is any stage that is NOT free
            has_paid_stage = self.stages.filter(is_free=False).exists()
            # If has_paid_stage is True, is_premium should be True
            # If has_paid_stage is False (all free), is_premium should be False
            if self.is_premium != has_paid_stage:
                self.is_premium = has_paid_stage
                self.save(update_fields=['is_premium'])

    def get_free_stages_count(self):
        return self.stages.filter(is_free=True).count()
    
    def update_stats(self):
        self.total_stages = self.stages.count()
        self.update_premium_status() # Also update premium status when stats update
        self.save(update_fields=['total_stages', 'is_premium'])


class RoadmapBundle(models.Model):
    """Bundle of multiple roadmaps sold together"""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    roadmaps = models.ManyToManyField(Roadmap, related_name='bundles')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    image = models.ImageField(upload_to='bundles/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - ₹{self.price}"
    
    def get_roadmaps_count(self):
        return self.roadmaps.count()


class Stage(models.Model):
    """A stage/level within a roadmap"""
    
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='stages')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    order = models.PositiveIntegerField(default=1)
    is_free = models.BooleanField('Free Access', default=False)
    required_xp = models.PositiveIntegerField('Required XP to Unlock', default=0)
    xp_reward = models.PositiveIntegerField('XP Reward on Completion', default=100)
    
    # Visual
    icon = models.CharField(max_length=50, default='fa-book')
    color = models.CharField(max_length=20, default='#6366f1')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['roadmap', 'order']
        unique_together = ['roadmap', 'order']
    
    def __str__(self):
        return f"{self.roadmap.title} - Stage {self.order}: {self.title}"
    
    def get_topics_count(self):
        return self.topics.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.roadmap.update_premium_status()

    def delete(self, *args, **kwargs):
        roadmap = self.roadmap
        super().delete(*args, **kwargs)
        roadmap.update_premium_status()


class Topic(models.Model):
    """Individual topic/lesson within a stage"""
    
    CONTENT_TYPE_CHOICES = [
        ('text', 'Text Content'),
        ('video', 'Video'),
        ('quiz', 'Quiz Only'),
        ('resource', 'External Resource'),
    ]
    
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    content = models.TextField('Content (Markdown supported)')
    
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='text')
    video_url = models.URLField('Video URL', blank=True)
    resource_url = models.URLField('Resource URL', blank=True)
    
    order = models.PositiveIntegerField(default=1)
    duration_minutes = models.PositiveIntegerField('Duration (minutes)', default=10)
    xp_reward = models.PositiveIntegerField('XP Reward', default=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['stage', 'order']
    
    def __str__(self):
        return f"{self.stage.title} - {self.title}"


class Quiz(models.Model):
    """Quiz for a stage or topic"""
    
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    passing_score = models.PositiveIntegerField('Passing Score (%)', default=70)
    xp_reward = models.PositiveIntegerField('XP Reward', default=50)
    time_limit = models.PositiveIntegerField('Time Limit (minutes)', default=10)
    
    is_required = models.BooleanField('Required to Complete Stage', default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Quizzes'
    
    def __str__(self):
        return f"Quiz: {self.title}"
    
    def get_questions_count(self):
        return self.questions.count()


class QuizQuestion(models.Model):
    """Individual question in a quiz"""
    
    QUESTION_TYPE_CHOICES = [
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
        ('truefalse', 'True/False'),
    ]
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='single')
    
    explanation = models.TextField('Answer Explanation', blank=True)
    order = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ['quiz', 'order']
    
    def __str__(self):
        return f"Q{self.order}: {self.question_text[:50]}"


class QuizOption(models.Model):
    """Answer options for a quiz question"""
    
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ['question', 'order']
    
    def __str__(self):
        return self.option_text


class UserRoadmapEnrollment(models.Model):
    """Tracks user enrollment in roadmaps"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='enrollments')
    
    enrolled_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)
    
    # Progress
    current_stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['user', 'roadmap']
    
    def __str__(self):
        return f"{self.user.email} - {self.roadmap.title}"
    
    def get_progress_percentage(self):
        total_topics = Topic.objects.filter(stage__roadmap=self.roadmap).count()
        if total_topics == 0:
            return 0
        completed = UserTopicProgress.objects.filter(
            user=self.user,
            topic__stage__roadmap=self.roadmap,
            is_completed=True
        ).count()
        return int((completed / total_topics) * 100)


class UserTopicProgress(models.Model):
    """Tracks user progress on individual topics"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_progress')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='user_progress')
    
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_spent = models.PositiveIntegerField('Time Spent (seconds)', default=0)
    
    class Meta:
        unique_together = ['user', 'topic']
    
    def __str__(self):
        return f"{self.user.email} - {self.topic.title}"


class UserQuizAttempt(models.Model):
    """Records quiz attempts by users"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    
    score = models.PositiveIntegerField(default=0)
    passed = models.BooleanField(default=False)
    answers = models.JSONField(default=dict)  # Stores question:answer mapping
    
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_taken = models.PositiveIntegerField('Time Taken (seconds)', default=0)
    
    class Meta:
        ordering = ['-started_at']
    
    def __str__(self):
        return f"{self.user.email} - {self.quiz.title} ({self.score}%)"


class UserGamification(models.Model):
    """Gamification stats for users (XP, Level, Streak)"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gamification')
    
    total_xp = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    
    current_streak = models.PositiveIntegerField('Current Daily Streak', default=0)
    longest_streak = models.PositiveIntegerField('Longest Streak', default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    
    total_time_spent = models.PositiveIntegerField('Total Time (minutes)', default=0)
    topics_completed = models.PositiveIntegerField(default=0)
    quizzes_passed = models.PositiveIntegerField(default=0)
    roadmaps_completed = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email} - Level {self.level} ({self.total_xp} XP)"
    
    def add_xp(self, amount):
        """Add XP and update level"""
        self.total_xp += amount
        # Level formula: Level = floor(total_xp / 500) + 1
        new_level = (self.total_xp // 500) + 1
        if new_level > self.level:
            self.level = new_level
        self.save()
    
    def update_streak(self):
        """Update daily streak"""
        today = timezone.now().date()
        if self.last_activity_date:
            if self.last_activity_date == today:
                return  # Already logged today
            elif self.last_activity_date == today - timezone.timedelta(days=1):
                self.current_streak += 1
            else:
                self.current_streak = 1
        else:
            self.current_streak = 1
        
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
        
        self.last_activity_date = today
        self.save()


class XPTransaction(models.Model):
    """Log of XP earned"""
    
    ACTION_CHOICES = [
        ('topic_complete', 'Topic Completed'),
        ('quiz_pass', 'Quiz Passed'),
        ('stage_complete', 'Stage Completed'),
        ('roadmap_complete', 'Roadmap Completed'),
        ('streak_bonus', 'Streak Bonus'),
        ('admin_bonus', 'Admin Bonus'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='xp_transactions')
    amount = models.IntegerField()
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} +{self.amount} XP ({self.action})"


class SiteSetting(models.Model):
    """Singleton model for site-wide settings"""
    
    maintenance_mode = models.BooleanField(default=False)
    maintenance_message = models.TextField(default="We are currently undergoing maintenance. Please check back later.")
    
    def save(self, *args, **kwargs):
        if not self.pk and SiteSetting.objects.exists():
            # If trying to create a new instance when one exists, update the existing one
            return SiteSetting.objects.first()
        return super(SiteSetting, self).save(*args, **kwargs)
        
    def __str__(self):
        return "Site Configuration"
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
