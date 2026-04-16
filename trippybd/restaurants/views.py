from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Restaurant
from cities.models import City

# View for listing all restaurants in a city
def restaurant_list(request, city_id):
    city = City.objects.get(id=city_id)
    restaurants = Restaurant.objects.filter(city=city)
    return render(request, 'restaurants/restaurant_list.html', {'city': city, 'restaurants': restaurants})

# View for displaying details of a specific restaurant
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})