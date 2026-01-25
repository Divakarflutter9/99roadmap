"""
Payment Admin Configuration
"""

from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription, Payment, Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percent', 'valid_from', 'valid_to', 'usage_limit', 'used_count', 'active', 'is_valid_now']
    list_filter = ['active', 'valid_to']
    search_fields = ['code']
    list_editable = ['active']
    filter_horizontal = ['valid_for_plans', 'valid_for_roadmaps', 'valid_for_bundles']
    
    def is_valid_now(self, obj):
        return obj.is_valid()
    is_valid_now.boolean = True
    is_valid_now.short_description = 'Currently Valid'


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_type', 'price', 'duration_days', 'is_active', 'is_popular']
    list_filter = ['duration_type', 'is_active', 'is_popular']
    list_editable = ['is_active', 'is_popular']
    search_fields = ['name', 'description']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'status', 'start_date', 'end_date', 'days_left']
    list_filter = ['status', 'plan']
    search_fields = ['user__email', 'user__full_name']
    readonly_fields = ['created_at', 'updated_at']
    
    def days_left(self, obj):
        return obj.days_remaining()
    days_left.short_description = 'Days Remaining'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'subscription_plan', 'amount', 'status', 'coupon_code_display', 'created_at']
    list_filter = ['status', 'created_at', 'subscription_plan']
    search_fields = ['order_id', 'user__email', 'user__phone', 'payment_id', 'cf_order_id']
    readonly_fields = ['created_at', 'updated_at', 'cf_response']
    
    def coupon_code_display(self, obj):
        return obj.coupon.code if obj.coupon else '-'
    coupon_code_display.short_description = 'Coupon'

    fieldsets = (
        ('Basic Info', {'fields': ('user', 'subscription_plan', 'amount', 'coupon')}),
        ('Order Details', {'fields': ('order_id', 'payment_id', 'status')}),
        ('Cashfree Details', {'fields': ('cf_order_id', 'cf_payment_session_id', 'cf_response')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
