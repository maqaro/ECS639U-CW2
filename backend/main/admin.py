"""Admin configuration for the main application."""
from django.contrib import admin
from .models import Team, League, LeagueMembership


class LeagueMembershipInline(admin.TabularInline):
    """Inline admin interface for LeagueMembership model."""
    model = League.teams.through
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model."""
    list_display = (
        'name',
        'city',
        'captain',
        'coach',
        'year_founded'
    )
    search_fields = (
        'name',
        'city',
        'captain',
        'coach'
    )
    inlines = (LeagueMembershipInline,)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    """Admin interface for League model."""
    list_display = (
        'name',
        'location'
    )
    search_fields = (
        'name',
        'location'
    )


@admin.register(LeagueMembership)
class LeagueMembershipAdmin(admin.ModelAdmin):
    """Admin interface for LeagueMembership model."""
    list_display = (
        'team',
        'league',
        'still_active',
        'date_joined'
    )
    search_fields = (
        'team__name',
        'league__name'
    )
