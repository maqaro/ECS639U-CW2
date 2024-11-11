"""Views for the main application."""
import json
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Team, League, LeagueMembership
from datetime import date, datetime

def index_view(request):
    """Handles the index page"""
    return render(request, 'main/index.html', {
        'teams': Team.objects.all()
    }) 

def team_view(request, team_id):
    """Handles the team page"""
    return render(request, 'main/team.html', {
        'team': Team.objects.get(id=team_id) 
    })

def league_view(request, league_id):
    """Handles the league page"""
    return render(request, 'main/league.html', {
        'league': League.objects.get(id=league_id)
    })

def membership_view(request, membership_id):
    """Handles the membership page"""
    return render(request, 'main/membership.html', {
        'membership': LeagueMembership.objects.get(id=membership_id)
    })

@csrf_exempt  
def teams_api_view(request):
    """Handles the teams API and its CRUD operations"""
    if request.method == 'GET':
        return JsonResponse({
            'teams': [team.as_dict() for team in Team.objects.all()]
        })

    elif request.method == 'POST':
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
            
            team = get_object_or_404(Team, id=team_id)
            team.delete()
            return JsonResponse({'message': 'Team deleted successfully'}, status=200)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)

@csrf_exempt
def leagues_api_view(request):
    """Handles the leagues API and its CRUD operations"""
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

@csrf_exempt
def memberships_api_view(request):
    """Handles the memberships API and its CRUD operations"""
    if request.method == 'GET':
        memberships = LeagueMembership.objects.all()
        return JsonResponse({
            'memberships': [{
                'id': m.id,
                'team': m.team.as_dict(),
                'league': m.league.as_dict(),
                'still_active': m.still_active,
                'date_joined': m.date_joined.isoformat()
            } for m in memberships]
        })

    elif request.method == 'POST':
        try:
            print("Received request body:", request.body)  # Debug print
            data = json.loads(request.body)
            print("Parsed JSON data:", data)  # Debug print
            
            # Validate required fields
            if 'team_id' not in data or 'league_id' not in data:
                return JsonResponse({'error': 'team_id and league_id are required'}, status=400)

            # Get team and league
            try:
                team = Team.objects.get(id=data['team_id'])
            except Team.DoesNotExist:
                return JsonResponse({'error': f"Team with id {data['team_id']} does not exist"}, status=400)

            try:
                league = League.objects.get(id=data['league_id'])
            except League.DoesNotExist:
                return JsonResponse({'error': f"League with id {data['league_id']} does not exist"}, status=400)

            # Parse date if provided
            date_joined = data.get('date_joined')
            if date_joined:
                try:
                    date_joined = datetime.strptime(date_joined, '%Y-%m-%d').date()
                except ValueError:
                    return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)
            else:
                date_joined = date.today()

            # Create membership
            membership = LeagueMembership.objects.create(
                team=team,
                league=league,
                still_active=data.get('still_active', True),
                date_joined=date_joined
            )

            # Return response
            return JsonResponse({
                'id': membership.id,
                'team': team.as_dict(),
                'league': league.as_dict(),
                'still_active': membership.still_active,
                'date_joined': membership.date_joined.isoformat()
            }, status=201)

        except json.JSONDecodeError as e:
            print("JSON Decode Error:", str(e))  # Debug print
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print("Unexpected Error:", str(e))  # Debug print
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            membership = LeagueMembership.objects.get(id=data['id'])
            membership.delete()
            return JsonResponse({'message': 'Membership deleted successfully'})
        except (KeyError, LeagueMembership.DoesNotExist):
            return JsonResponse({'error': 'Membership not found'}, status=404)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            
            membership = LeagueMembership.objects.get(id=data['id'])
            
            if 'team_id' in data:
                team = Team.objects.get(id=data['team_id'])
                membership.team = team
            
            if 'league_id' in data:
                league = League.objects.get(id=data['league_id'])
                membership.league = league
            
            membership.still_active = data.get('still_active', membership.still_active)
            
            if 'date_joined' in data:
                membership.date_joined = datetime.strptime(data['date_joined'], '%Y-%m-%d').date()
            
            membership.save()
            
            # Format the response
            response_data = {
                'id': membership.id,
                'team': membership.team.as_dict(),
                'league': membership.league.as_dict(),
                'still_active': membership.still_active,
                'date_joined': membership.date_joined.strftime('%Y-%m-%d')
            }
            return JsonResponse(response_data)
            
        except LeagueMembership.DoesNotExist:
            return JsonResponse({'error': 'Membership not found'}, status=404)
        except (Team.DoesNotExist, League.DoesNotExist) as e:
            return JsonResponse({'error': str(e)}, status=404)
        except Exception as e:
            print("Error:", str(e))  # Debug log
            return JsonResponse({'error': str(e)}, status=500)

