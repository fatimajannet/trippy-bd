from django.shortcuts import render, get_object_or_404
from .models import City
from hotels.models import Hotel
from wishlist.models import Wishlist

def home(request):
    return render(request, 'index.html')

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

# In your city detail view (cities/views.py or wherever it lives)
def city_details(request, city_id):
    city = get_object_or_404(City, id=city_id)
    attractions = city.attraction_set.all()  # adjust as needed
    hotels = city.hotel_set.all()            # adjust as needed
    
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, city=city).exists()
    
    context = {
        'city': city,
        'attractions': attractions,
        'hotels': hotels,
        'in_wishlist': in_wishlist,
    }
    return render(request, 'cities/city_details.html', context)