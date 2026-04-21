from django.shortcuts import render, get_object_or_404
from .models import Hotel
from cities.models import City

def hotel_list(request):
    hotels = Hotel.objects.select_related('city').all()
    cities = City.objects.all()
    return render(request, 'hotels/hotel_list.html', {
        'hotels': hotels,
        'cities': cities,
    })

def hotel_list_by_city(request, city_id):
    city   = get_object_or_404(City, pk=city_id)
    hotels = Hotel.objects.filter(city=city).select_related('city')
    cities = City.objects.all()
    return render(request, 'hotels/hotel_list.html', {
        'hotels':        hotels,
        'selected_city': city,
        'cities':        cities,
    })

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel.objects.select_related('city'), pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})