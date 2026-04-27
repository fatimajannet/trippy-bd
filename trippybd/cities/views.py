from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import City
from attractions.models import Attraction
from hotels.models import Hotel
from agencies.models import Agency, Guide
from restaurants.models import Restaurant

def home(request):
    context = {
        'city_count': City.objects.count(),
        'attraction_count': Attraction.objects.count(),
        'hotel_count': Hotel.objects.count(),
        'restaurant_count': Restaurant.objects.count(),
        'agency_count': Agency.objects.count(),
        'guide_count': Guide.objects.count(),
    }
    return render(request, 'index.html', context)

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})

# In your city detail view (cities/views.py or wherever it lives)
def city_details(request, city_id):
    # 1. Fetch the city or 404
    city = get_object_or_404(City, id=city_id)
    
    # 2. Fetch related data
    # Note: Use 'city.hotel_set.all()' if your Hotel model has a ForeignKey to City
    attractions = city.attraction_set.all()
    hotels = city.hotel_set.all()
    
    # 3. Initialize user-specific states
    in_wishlist = False
    is_visited = False
    
    # 4. Check status if user is logged in
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, city=city).exists()
        is_visited = TravelHistory.objects.filter(user=request.user, city=city).exists()
    
    # 5. Build context
    context = {
        'city': city,
        'attractions': attractions,
        'hotels': hotels,
        'in_wishlist': in_wishlist,
        'is_visited': is_visited,
    }
    
    return render(request, 'cities/city_details.html', context)