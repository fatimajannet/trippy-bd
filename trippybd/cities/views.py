from django.shortcuts import render, get_object_or_404
from .models import City
from hotels.models import Hotel

def home(request):
    return render(request, 'index.html')

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

def city_details(request, city_id):
    city   = get_object_or_404(City, id=city_id)
    hotels = Hotel.objects.filter(city=city)
    return render(request, 'cities/city_details.html', {
        'city':   city,
        'hotels': hotels,
    })