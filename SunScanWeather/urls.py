from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("removecity", views.removeCity, name="removecity"),
    path("removeallcities", views.removeAllCities, name="removeallcities")
]
