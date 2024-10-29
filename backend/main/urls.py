from django.contrib import admin
from django.urls import path, include
from .views import index_view, team_view, teams_api_view

urlpatterns = [
    path('', index_view, name='index'),
    path('team/<int:team_id>', team_view, name='team'),
    path('api/teams/', teams_api_view, name='teams_api'), 
]
