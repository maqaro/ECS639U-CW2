from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

def index_view(request):
    return render(request, 'main/index.html', {
        'teams': Team.objects.all()
    }) 

def team_view(request, team_id):
    return render(request, 'main/team.html', {
        'team': Team.objects.get(id=team_id) 
    })