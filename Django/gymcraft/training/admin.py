from django.contrib import admin
from .models import User, WorkoutDetail, Exercise, MuscleGroup

# Register your models here.
admin.site.register(User)
admin.site.register(WorkoutDetail)
admin.site.register(Exercise)
admin.site.register(MuscleGroup)