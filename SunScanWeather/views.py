from django.shortcuts import render
import requests


def index(request):
    # URL of openweathermap with query for city, units of temperature, and API key
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=73605a430c8b6d3d7bb18f3851d12e34'
    city = 'Houston'

    # Request from API
    req = requests.get(url.format(city)).json()

    # Pull values we want from API
    city_weather = {
        'city': city,
        'temperature': req['main']['temp'],
        'description': req['weather'][0]['description'],
        'icon': req['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}

    return render(request, 'index.html', context)
