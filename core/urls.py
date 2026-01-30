"""
URL Configuration for core app
"""

from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/<str:token>/', views.reset_password_view, name='reset_password'),
    path('profile/', views.profile_view, name='profile'),
    
    # Home & Dashboard
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('set-goal/', views.set_weekly_goal, name='set_weekly_goal'),
    
    # Roadmaps
    path('roadmaps/', views.roadmap_list_view, name='roadmap_list'),
    path('roadmap/<slug:slug>/', views.roadmap_detail_view, name='roadmap_detail'),
    path('roadmap/<int:roadmap_id>/download-pdf/', views.download_roadmap_pdf, name='download_roadmap_pdf'),
    path('roadmap/<slug:roadmap_slug>/stage/<int:stage_order>/', views.stage_detail_view, name='stage_detail'),
    
    # Topics
    path('topic/<int:topic_id>/', views.topic_view, name='topic_view'),
    path('topic/<int:topic_id>/complete/', views.mark_topic_complete, name='mark_topic_complete'),
    
    # Quizzes
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('stage/<int:stage_id>/quiz/', views.quiz_view, name='stage_quiz'),
    path('quiz/result/<int:attempt_id>/', views.quiz_result_view, name='quiz_result'),
    
    # Leaderboard
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    
    # Static Pages
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('refund-policy/', views.refund_policy_view, name='refund_policy'),
]
