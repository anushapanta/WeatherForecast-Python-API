from django.shortcuts import render
import requests

from weatherforecast.forms import CityForm
from .models import City


def index(request):
    cities = City.objects.all()  # return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2c52bf0c03cf4746f59dfe717e2fd36c'

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data,'form' : form}

    return render(request, 'pages/index.html', context)  # returns the index.html template
