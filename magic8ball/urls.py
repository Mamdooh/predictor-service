from django.urls import path
from . import views

app_name = 'magic8ball'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('api/predict/', views.api_predict, name='api_predict'),
    path('health/', views.health, name='health'),
]
