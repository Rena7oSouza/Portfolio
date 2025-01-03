from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('setworkout/', views.setWorkout_view, name='setWorkout'),
    path('mytraining/<int:day_of_week>/', views.myTraining_view, name='myTraining'),
    path('delete_workout_detail/<int:workout_detail_id>/', views.delete_workout_detail_view, name='delete_workout_detail'),
]