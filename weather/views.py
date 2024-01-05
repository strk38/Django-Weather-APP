import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    cities=City.objects.all()
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a79c348ffad680ebc3516e408d438af0'

    #city='Las Vegas'
    if request.method =='POST':
        form=CityForm(request.POST)
        form.save()

    form= CityForm()


    weather_data=[]

    for city in cities :
        r= requests.get(url.format(city)).json()
        
        city_weather={
            'city': r['name'],
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        #print(city_weather)
        weather_data.append(city_weather)

    context = { 'weather_data' : weather_data, 'form': form}

    return render(request,'weather/weather.html', context)