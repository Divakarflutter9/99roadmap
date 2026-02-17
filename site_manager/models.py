from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class UserSession(models.Model):
    """Tracks user behavior for the AI Guide"""
    session_key = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    # Behavior Data
    page_views = models.JSONField(default=dict)  # {"/pricing": 2, "/python": 1}
    interests = models.JSONField(default=dict)   # {"python": 5, "frontend": 2}
    
    is_bounced = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Session {self.session_key} ({self.user if self.user else 'Anon'})"

class GuideCampaign(models.Model):
    """Rules for the AI Guide"""
    TRIGGER_CHOICES = [
        ('page_view', 'Page View'),
        ('time_on_page', 'Time on Page (sec)'),
        ('click', 'Element Click'),
        ('idle', 'User Idle'),
        ('exit_intent', 'Exit Intent'),
    ]
    
    ACTION_CHOICES = [
        ('message', 'Show Message'),
        ('overlay', 'Show Overlay'),
        ('redirect', 'Redirect'),
    ]
    
    name = models.CharField(max_length=100)
    trigger_event = models.CharField(max_length=20, choices=TRIGGER_CHOICES)
    trigger_condition = models.JSONField(default=dict, help_text='{"path": "/pricing", "value": 30}')
    
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES, default='message')
    message_content = models.TextField()
    
    cta_text = models.CharField(max_length=50, blank=True)
    cta_link = models.CharField(max_length=200, blank=True)
    
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
