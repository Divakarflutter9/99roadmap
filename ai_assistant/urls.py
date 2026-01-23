"""
URLs for AI assistant app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.ai_chat_view, name='ai_chat'),
    path('ask/', views.ai_ask, name='ai_ask'),
    path('explain/<int:topic_id>/', views.ai_explain_topic, name='ai_explain_topic'),
]
