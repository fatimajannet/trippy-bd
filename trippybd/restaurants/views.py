from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from cities.models import City

def restaurant_list(request):
    restaurants = Restaurant.objects.select_related('city').all()
    cities      = City.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {
        'restaurants': restaurants,
        'cities':      cities,
    })

def restaurant_list_by_city(request, city_id):
    city        = get_object_or_404(City, pk=city_id)
    restaurants = Restaurant.objects.filter(city=city).select_related('city')
    cities      = City.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {
        'restaurants':   restaurants,
        'selected_city': city,
        'cities':        cities,
    })

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(
        Restaurant.objects.select_related('city'), pk=pk
    )
    return render(request, 'restaurants/restaurant_detail.html', {
        'restaurant': restaurant
    })