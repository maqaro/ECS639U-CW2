import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Team, League

def index_view(request):
    return render(request, 'main/index.html', {
        'teams': Team.objects.all()
    }) 

def team_view(request, team_id):
    return render(request, 'main/team.html', {
        'team': Team.objects.get(id=team_id) 
    })

def league_view(request, league_id):
    return render(request, 'main/league.html', {
        'league': League.objects.get(id=league_id)
    })

@csrf_exempt  
def teams_api_view(request):
    if request.method == 'GET':
        return JsonResponse({
            'teams': [team.as_dict() for team in Team.objects.all()]
        })

    elif request.method == 'POST':
        # Handle creating a new team
        try:
            data = json.loads(request.body)
            team = Team.objects.create(
                name=data['name'],
                city=data['city'],
                captain=data['captain'],
                coach=data['coach'],
                year_founded=data['year_founded']
            )
            return JsonResponse(team.as_dict(), status=201)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            team_id = data.get('id')
            if not team_id:
                return JsonResponse({'error': 'Team ID is required'}, status=400)
            
            team = Team.objects.get(id=team_id)
            team.name = data['name']
            team.city = data['city']
            team.captain = data['captain']
            team.coach = data['coach']
            team.year_founded = data['year_founded']
            team.save()
            return JsonResponse(team.as_dict(), status=200)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            team_id = data.get('id')
            if not team_id:
                return JsonResponse({'error': 'Team ID is required'}, status=400)
            
            team = Team.objects.get(id=team_id)
            team.delete()
            return JsonResponse({'message': 'Team deleted successfully'}, status=200)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    return HttpResponse(status=405) 

@csrf_exempt
def leagues_api_view(request):
    if request.method == 'GET':
        leagues = League.objects.all()
        data = {'leagues': [league.as_dict() for league in leagues]}
        return JsonResponse(data)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            league = League.objects.create(
                name=data['name'],
                location=data['location']
            )
            return JsonResponse(league.as_dict(), status=201)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            league_id = data.get('id')
            if not league_id:
                return JsonResponse({'error': 'League ID is required'}, status=400)
            
            league = League.objects.get(id=league_id)
            league.name = data['name']
            league.location = data['location']
            league.save()
            return JsonResponse(league.as_dict(), status=200)
        except League.DoesNotExist:
            return JsonResponse({'error': 'League not found'}, status=404)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            league_id = data.get('id')
            if not league_id:
                return JsonResponse({'error': 'League ID is required'}, status=400)
            
            league = League.objects.get(id=league_id)
            league.delete()
            return JsonResponse({'message': 'League deleted successfully'}, status=200)
        except League.DoesNotExist:
            return JsonResponse({'error': 'League not found'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    return HttpResponse(status=405)
