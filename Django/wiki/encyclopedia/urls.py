from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.getentry, name="content"),
    path("search", views.search, name="search"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("addPage", views.addPage, name="addPage"),
    path("editPage", views.editPage, name="editPage"),
    path("savePage", views.savePage, name="savePage")
]

