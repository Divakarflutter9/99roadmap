from django.urls import path
from . import views

urlpatterns = [
    path('api/guide/track/', views.track_action, name='track_guide_action'),
    path('api/guide/suggest-roadmap/', views.suggest_roadmap, name='suggest_roadmap'),
    path('enroll/<int:roadmap_id>/', views.enroll_and_redirect, name='enroll_redirect'), # NEW Simple Link
    # path('api/guide/ext/enroll/', views.enroll_from_guide, name='enroll_from_guide'), # Deprecated/JSON
    path('api/guide/suggest-roadmap/', views.suggest_roadmap, name='suggest_roadmap'),
]
