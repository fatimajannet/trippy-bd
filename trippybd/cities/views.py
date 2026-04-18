from django.shortcuts import render, get_object_or_404
from .models import City

# View for the city list page
def city_list(request):
    cities = City.objects.all()  # Fetch all cities
    return render(request, 'cities/city_list.html', {'cities': cities})

# View for the city details page
def city_details(request, city_id):
    city = get_object_or_404(City, id=city_id)  # Fetch the city by id
    return render(request, 'cities/city_details.html', {'city': city})