from django.contrib import admin
from django.urls import path, include
from .views import index_view, team_view, teams_api_view, league_view, leagues_api_view

urlpatterns = [
    path('', index_view, name='index'),
    path('api/team/<int:team_id>', team_view, name='team'),
    path('api/teams/', teams_api_view, name='teams_api'), 
    path('api/league/<int:league_id>', league_view, name='league'),
    path('api/leagues/', leagues_api_view, name='leagues_api'), 
]
