from django.contrib import admin
from .models import Team, League

class LeagueMembershipInline(admin.TabularInline):
    model = League.teams.through
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'captain', 'coach', 'year_founded')
    search_fields = ('name', 'city', 'captain', 'coach')
    inlines = (LeagueMembershipInline,)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')