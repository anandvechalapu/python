# Urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('validate_policy/', views.validate_policy, name='validate_policy'),
    path('policy_confirmation/', views.policy_confirmation, name='policy_confirmation'),
]