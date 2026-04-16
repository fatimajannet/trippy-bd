# hotels/views.py
from django.shortcuts import render
from .models import Hotel

# View for listing hotels based on the city
def hotel_list(request, city_id):
    hotels = Hotel.objects.filter(city_id=city_id)
    city = hotels.first().city if hotels else None
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels, 'city': city})

# View for showing details of a single hotel
def hotel_detail(request, pk):
    hotel = Hotel.objects.get(pk=pk)  # Get the hotel by its primary key (ID)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})