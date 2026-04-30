from django.shortcuts import render, get_object_or_404
from cities.models import City
from hotels.models import Room
from restaurants.models import Restaurant
from attractions.models import Attraction
from transportation.models import Transportation
from agencies.models import Guide
from .utils import calculate_custom_budget

from django.shortcuts import render, redirect # Add redirect
from django.urls import reverse

def budget_planner(request):
    cities = City.objects.all()
    
    if request.method == "POST":
        city_name = request.POST.get('city_name')
        days = request.POST.get('days', 1)
        stay_tier = request.POST.get('stay_tier', 'mid')
        hire_guide = request.POST.get('hire_guide') == 'on'
        
        selected_city = City.objects.filter(name__iexact=city_name).first()
        
        if selected_city:
            # Redirect to the details view
            # We pass the selected tier and the days as a GET parameter
            url = reverse('plan_details', kwargs={
                'city_id': selected_city.id, 
                'tier': stay_tier
            })
            # Include 'days' and 'guide' in the query string
            return redirect(f"{url}?days={days}&guide={hire_guide}")

    return render(request, 'budget/planner.html', {'cities': cities})

def plan_details(request, city_id, tier):
    city = get_object_or_404(City, id=city_id)
    days = int(request.GET.get('days', 1))
    # Capture the guide preference from the URL
    hire_guide = request.GET.get('guide') == 'True'
    
    # Selection logic based on tier
    if tier == 'budget' or tier == 'low':
        room = Room.objects.filter(hotel__city=city).order_by('r_price').first()
        restaurant = Restaurant.objects.filter(city=city).order_by('average_price').first()
        guide = Guide.objects.filter(agency__city=city).order_by('price_per_day').first() if hire_guide else None
        transport = Transportation.objects.filter(city=city).order_by('apprx_cost').first()
    elif tier == 'premium' or tier == 'high':
        room = Room.objects.filter(hotel__city=city).order_by('-r_price').first()
        restaurant = Restaurant.objects.filter(city=city).order_by('-average_price').first()
        guide = Guide.objects.filter(agency__city=city).order_by('-price_per_day').first() if hire_guide else None
        transport = Transportation.objects.filter(city=city).order_by('-apprx_cost').first()
    else: # Standard (Mid-range)
        rooms = Room.objects.filter(hotel__city=city).order_by('r_price')
        room = rooms[len(rooms)//2] if rooms.exists() else None
        rests = Restaurant.objects.filter(city=city).order_by('average_price')
        restaurant = rests[len(rests)//2] if rests.exists() else None
        guides = Guide.objects.filter(agency__city=city).order_by('price_per_day')
        guide = (guides[len(guides)//2] if guides.exists() else None) if hire_guide else None
        trans = Transportation.objects.filter(city=city).order_by('apprx_cost')
        transport = trans[len(trans)//2] if trans.exists() else None

    attractions = Attraction.objects.filter(city=city)
    
    # Calculate costs
    h_total = (room.r_price * days) if room else 0
    f_total = (restaurant.average_price * 3 * days) if restaurant else 0
    g_total = (guide.price_per_day * days) if (guide and hire_guide) else 0
    a_total = sum(attr.entry_fee for attr in attractions)
    t_total = 2* (transport.apprx_cost if transport else 0)
    
    grand_total = h_total + f_total + g_total + a_total + t_total

    context = {
        'city': city, 'tier': tier, 'days': days, 'hire_guide': hire_guide,
        'room': room, 'restaurant': restaurant, 'guide': guide,
        'transport': transport, 'attractions': attractions,
        'h_total': h_total, 'f_total': f_total, 'g_total': g_total,
        'a_total': a_total, 't_total': t_total, 'grand_total': grand_total
    }
    return render(request, 'budget/plan_details.html', context)