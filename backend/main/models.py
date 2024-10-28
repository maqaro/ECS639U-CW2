from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    year_founded = models.IntegerField(default=1900)

    def __str__(self):
        return f"{self.name} - ({self.city})"
    
    # class League(models.Model):
    #     name = models.CharField(max_length=100)
    #     country = models.CharField(max_length=100)
    #     teams = models.ManyToManyField(Team, related_name='teams')

    #     def __str__(self):
    #         return f"{self.name} - ({self.country})"
