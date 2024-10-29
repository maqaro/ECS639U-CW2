from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    year_founded = models.IntegerField(default=1900)

    def __str__(self):
        return f"{self.name} - ({self.city})"
    
    def as_dict(self):
        return {
            "name": self.name,
            "city": self.city,
            "captain": self.captain,
            "coach": self.coach,
            "year_founded": self.year_founded,
        }
    
    
class LeagueMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey('League', on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team.name} - {self.league.name}"
    
    
class League(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, through='LeagueMembership')

    def __str__(self):
        return f"{self.name} - ({self.location})"
    
    def as_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "teams": [team.as_dict() for team in self.teams.all()]
        }