from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fea0b25e7b70cd716490167e3ff778b6'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json()  # request the API data and convert theYOUR_APP_KEY JSON to Python data types

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return render(request, 'pages/index.html', context)  # returns the index.html template
