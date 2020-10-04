from django.shortcuts import render, redirect
import requests
from weather.models import CityName
from weather.forms import CityForm

# Create your views here.
def index(request):
    owm_api_key = 'owm_api_key'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+owm_api_key
    error_msg = None
    message_class = None

    if request.method == 'POST':
        # print("TRANSMIT ", request.POST)
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = CityName.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                response_new = requests.get(url.format(new_city)).json()
                if response_new['cod'] == 200:
                    form.save()
                else:
                    error_msg = "City not found!"
            else:
                error_msg = "City weather is already available!"

        if error_msg:
            message_class = 'is-danger'
        else:
            error_msg = f'Weather of {new_city} fetched successfully!'
            message_class = 'is-success'

        # print("==> ", error_msg, message_class)

    form = CityForm()

    cities = CityName.objects.all()
    weather_data = list()

    for city in cities:
        response = requests.get(url.format(city)).json()
        # print(response.text)

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    # print(weather_data)
    context = {
                'weather_data': weather_data,
                'form': form,
                'message': error_msg,
                'message_class': message_class
                }

    return render(request, 'weather/weather.html', context=context)

def delete_city(request, city_name):
    # print("===> ", request.POST, city_name)
    CityName.objects.filter(name=city_name).delete()
    return redirect("weather_home")

def home(request):
    # print("===> On home page")
    return render(request, 'weather/index.html')
