from django.shortcuts import render, get_object_or_404
from .models import City
from hotels.models import Hotel


# View for the city list page
def city_list(request):
    cities = City.objects.all()  # Fetch all cities
    return render(request, 'cities/city_list.html', {'cities': cities})

# View for the city details page
def city_details(request, city_id):
    # Fetch the city using the city_id, or show a 404 page if it doesn't exist
    city = get_object_or_404(City, id=city_id)
    
    # Fetch all hotels related to this city
    hotels = Hotel.objects.filter(city=city)
    
    return render(request, 'cities/city_details.html', {'city': city, 'hotels': hotels})