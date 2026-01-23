"""
Payment Models for 99Roadmap
Handles subscriptions and Cashfree payment integration
"""

from django.db import models
from django.conf import settings
from core.models import User, Roadmap, RoadmapBundle
from django.utils import timezone


class Coupon(models.Model):
    """Discount coupons"""
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(help_text="Discount percentage (0-100)")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    usage_limit = models.PositiveIntegerField(default=100)
    used_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.code} - {self.discount_percent}%"
        
    def is_valid(self):
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to and self.used_count < self.usage_limit
class SubscriptionPlan(models.Model):
    """Subscription plans available"""
    
    DURATION_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
        ('lifetime', 'Lifetime'),
    ]
    
    name = models.CharField(max_length=100)
    duration_type = models.CharField(max_length=20, choices=DURATION_CHOICES)
    duration_days = models.PositiveIntegerField(help_text='Number of days for this plan')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, help_text='List of features')
    
    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class UserSubscription(models.Model):
    """User subscription records"""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='expired')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    auto_renew = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Subscription'
    
    def __str__(self):
        return f"{self.user.email} - {self.plan.name if self.plan else 'No Plan'}"
    
    def is_active(self):
        return self.status == 'active' and self.end_date and self.end_date > timezone.now()
    
    def days_remaining(self):
        if self.is_active():
            return (self.end_date - timezone.now()).days
        return 0


class Payment(models.Model):
    """Payment transaction records"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    
    # What is being purchased?
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    roadmap = models.ForeignKey(Roadmap, on_delete=models.SET_NULL, null=True, blank=True)
    bundle = models.ForeignKey(RoadmapBundle, on_delete=models.SET_NULL, null=True, blank=True)
    
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    
    order_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, blank=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Cashfree specific fields
    cf_order_id = models.CharField(max_length=100, blank=True)
    cf_payment_session_id = models.CharField(max_length=255, blank=True)
    cf_response = models.JSONField(default=dict, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - ₹{self.amount} ({self.status})"
