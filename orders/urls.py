from django.urls import path
from . import apiviews

urlpatterns = [
    path('orders/', views.members, name='members'),
]