"""
URL configuration for predictor project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('magic8ball.urls')),
]
