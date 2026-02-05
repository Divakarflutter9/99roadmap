"""
URLs for payments app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.subscription_plans_view, name='subscription_plans'),
    path('buy/<str:item_type>/<int:item_id>/', views.initiate_payment, name='initiate_payment'),
    path('callback/<int:payment_id>/', views.payment_callback, name='payment_callback'),
    path('webhook/', views.payment_webhook, name='payment_webhook'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('manager/', views.manager_panel_view, name='manager_panel'),
]
