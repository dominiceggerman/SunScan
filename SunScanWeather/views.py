from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    # URL of openweathermap with query for city, units of temperature, and API key
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=73605a430c8b6d3d7bb18f3851d12e34"

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    # Get all cities from database
    cities = City.objects.all()

    # Create a list for all of the API data
    weather_data = []

    for city in cities:

        # Request from API
        req = requests.get(url.format(city)).json()

        # Pull values we want from API
        city_weather = {
            "city": city.name,
            "temperature": req["main"]["temp"],
            "min_temp": req["main"]["temp_min"],
            "max_temp": req["main"]["temp_max"],
            "humidity": req["main"]["humidity"],
            "description": req["weather"][0]["description"],
            "icon": req["weather"][0]["icon"],
            "wind": req["wind"]["speed"],
        }

        # Append data
        weather_data.append(city_weather)

    context = {"weather_data": weather_data, "form": form}

    return render(request, "index.html", context)
