from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    youtube_embed = models.TextField(null=True)

    def __str__(self):
        return self.name


DAYS_OF_WEEK_CHOICES = [
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
]


class WorkoutDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    day_of_week = models.PositiveSmallIntegerField(choices=DAYS_OF_WEEK_CHOICES, default=1)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    repetitions = models.IntegerField(default=0)
    load = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)

    def __str__(self):
        days_of_week_dict = dict(DAYS_OF_WEEK_CHOICES)
        day_name = days_of_week_dict.get(self.day_of_week, 'Unknown')
        return f"{self.user.username}'s Workout {day_name}- {self.muscle_group.name} - {self.exercise}"
