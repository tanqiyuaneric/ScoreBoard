from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teamLogos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=100)
    team1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team2')
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    team1_total_score = models.IntegerField(default=0)
    team2_total_score = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    timer_start = models.IntegerField(default=0, blank=True)
    timer_end = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.name}: {self.team1} vs {self.team2}"


class CurrentRace(models.Model):
    race = models.ForeignKey(Race, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.race)