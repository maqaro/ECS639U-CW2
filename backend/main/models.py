"""Models for the main application."""
from django.db import models
from datetime import date


class Team(models.Model):
    """Team model representing a sports team."""
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    year_founded = models.IntegerField(default=1900)

    def __str__(self):
        """Return string representation of Team."""
        return f"{self.name} - ({self.city})"

    def as_dict(self):
        """Return dictionary representation of Team."""
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "captain": self.captain,
            "coach": self.coach,
            "year_founded": self.year_founded,
        }


class LeagueMembership(models.Model):
    """Model representing membership of a team in a league."""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey('League', on_delete=models.CASCADE)
    still_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=date.today)

    def __str__(self):
        """Return string representation of LeagueMembership."""
        return f"{self.team.name} - {self.league.name}"


class League(models.Model):
    """League model representing a sports league."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    teams = models.ManyToManyField(
        Team,
        through='LeagueMembership'
    )

    def __str__(self):
        """Return string representation of League."""
        return f"{self.name} - ({self.location})"

    def as_dict(self):
        """Return dictionary representation of League."""
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "teams": [team.as_dict() for team in self.teams.all()]
        }