from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team

def index_view(request):
    return render(request, 'main/index.html', {
        'teams': Team.objects.all()
    }) 

def team_view(request, team_id):
    return render(request, 'main/team.html', {
        'team': Team.objects.get(id=team_id) 
    })

def teams_api_view(request):
    if request.method == 'GET':
        return JsonResponse({
            'teams':[
                        team.as_dict() 
                        for team in Team.objects.all()
                    ]
        })
    
    # if request.method == 'POST':
    #     team = Team.objects.create(
    #         name=request.POST['name'],
    #         city=request.POST['city'],
    #         captain=request.POST['captain'],
    #         coach=request.POST['coach'],
    #         year_founded=request.POST['year_founded']
    #     )
    #     return JsonResponse(team.as_dict())

    return HttpResponse(status=405) 