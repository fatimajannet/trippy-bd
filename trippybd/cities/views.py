from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import City
from attractions.models import Attraction
from hotels.models import Hotel
from agencies.models import Agency, Guide
from restaurants.models import Restaurant
from wishlist.models import Wishlist
from travel_history.models import TravelHistory
from django.contrib.contenttypes.models import ContentType
from review.models import Review
from emergency_services.models import EmergencyService

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
    attractions = city.attraction_set.all()
    hotels = city.hotel_set.all()
    restaurants = city.restaurant_set.all()
    city_type = ContentType.objects.get_for_model(city)
    reviews = Review.objects.filter(content_type=city_type, object_id=city.id)
    services = city.emergency_services.all()

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
        'restaurants': restaurants,
        'reviews': reviews,        
        'in_wishlist': in_wishlist,
        'is_visited': is_visited,
        'services': services

    }
    
    return render(request, 'cities/city_details.html', context)