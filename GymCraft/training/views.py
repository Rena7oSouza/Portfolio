from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, WorkoutDetail, Exercise, MuscleGroup
from django.contrib.auth import login, logout, authenticate 
from django.db import IntegrityError
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "training/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "training/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = ""

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "training/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "training/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "training/register.html")


def home_view(request):
    if request.user.is_authenticated:
        today = datetime.now().weekday() + 1  
        workout_details = WorkoutDetail.objects.filter(user=request.user, day_of_week=today)
        muscle_group_ids = workout_details.values_list('muscle_group__id', flat=True).distinct()
        muscle_groups = MuscleGroup.objects.filter(id__in=muscle_group_ids)
        exercises = Exercise.objects.filter(workoutdetail__user=request.user, workoutdetail__day_of_week=today).distinct() 
             
    else:
        workout_details = None
        muscle_groups = None
        exercises = None

    return render(request, "training/home.html", {
        "workout_details": workout_details,
        "muscle_groups": muscle_groups,
        "exercises": exercises
    })


def myTraining_view(request, day_of_week):
    if request.method == 'POST':
        workout_detail_id = request.POST.get('workout_detail_id')
        load = request.POST.get('load')
        sets = request.POST.get('sets')
        repetitions = request.POST.get('repetitions')
        
        try:
            workout_detail = WorkoutDetail.objects.get(pk=workout_detail_id)
            workout_detail.load = load
            workout_detail.sets = sets
            workout_detail.repetitions = repetitions
            workout_detail.save()
        except WorkoutDetail.DoesNotExist:
            return render(request, 'training/myTraining.html', {
                'message': 'WorkoutDetail not found'
            })

        return redirect('myTraining', day_of_week=day_of_week)
    
    workout_details = WorkoutDetail.objects.filter(user=request.user, day_of_week=day_of_week)
    muscle_group_ids = workout_details.values_list('muscle_group__id', flat=True).distinct()
    muscle_groups = MuscleGroup.objects.filter(id__in=muscle_group_ids)
    exercises = Exercise.objects.filter(workoutdetail__user=request.user, workoutdetail__day_of_week=day_of_week).distinct()
    days_of_week = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
    
    return render(request, 'training/myTraining.html', {
        'workout_details': workout_details,
        'days_of_week': days_of_week,
        'muscle_groups': muscle_groups,
        'selected_day_of_week': int(day_of_week),
        'exercises': exercises
    })

@login_required
def delete_workout_detail_view(request, workout_detail_id):
    if request.method == 'POST':
        workout_detail = get_object_or_404(WorkoutDetail, id=workout_detail_id, user=request.user)
        workout_detail.delete()
        return redirect('myTraining', day_of_week=workout_detail.day_of_week)
    return redirect('myTraining', day_of_week=request.GET.get('day_of_week', 1))

    
def setWorkout_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user = request.user
        day_of_week = data.get('day_of_week')
        if(day_of_week == None):
            day_of_week = 'Monday'
        day_of_week_mapping = {
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5,
            'Saturday': 6,
            'Sunday': 7,
        }
        day_of_week = day_of_week_mapping.get(day_of_week)
        exercise_id = data.get('exercise')[0]
        exercise = Exercise.objects.get(pk=exercise_id)
        repetitions = data.get('repetitions')
        sets = data.get('sets')
        loads = data.get('loads')

        existing_workout_detail = WorkoutDetail.objects.filter(user=user, day_of_week=day_of_week, exercise=exercise).first()

        if existing_workout_detail:
            existing_workout_detail.repetitions = repetitions
            existing_workout_detail.sets = sets
            existing_workout_detail.load = loads
            existing_workout_detail.save()
        else:
            workout_detail = WorkoutDetail.objects.create(
                user=user,
                day_of_week=day_of_week,
                muscle_group=exercise.muscle_group,
                exercise=exercise,
                repetitions=repetitions,
                sets=sets,
                load=loads
            )

    exercises = Exercise.objects.all()
    muscle_groups = MuscleGroup.objects.all()
    days_of_week = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    return render(request, 'training/setWorkout.html', {'muscle_groups': muscle_groups, 'exercises': exercises, 'days_of_week': days_of_week})
