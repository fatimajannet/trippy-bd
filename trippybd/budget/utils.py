from django.db.models import Avg, Min, Max, Sum
from decimal import Decimal
from attractions.models import Attraction
from hotels.models import Room
from restaurants.models import Restaurant
from transportation.models import Transportation
from agencies.models import Guide

def calculate_custom_budget(city, days, hire_guide=True, transport_tier='mid', stay_tier='mid'):
    d = Decimal(days)

    attraction_cost = Attraction.objects.filter(city=city).aggregate(total=Sum('entry_fee'))['total'] or Decimal('0.00')

    room_stats = Room.objects.filter(hotel__city=city).aggregate(
        low=Min('r_price'), mid=Avg('r_price'), high=Max('r_price')
    )
    stay_daily = Decimal(room_stats[stay_tier] or 0)

    food_stats = Restaurant.objects.filter(city=city).aggregate(
        low=Min('average_price'), mid=Avg('average_price'), high=Max('average_price')
    )
    food_daily = Decimal(food_stats[stay_tier] or 0)

    trans_stats = Transportation.objects.filter(city=city).aggregate(
    low=Min('apprx_cost'), 
    mid=Avg('apprx_cost'), 
    high=Max('apprx_cost')
)
    transport_total = Decimal(trans_stats[transport_tier] or 0)

    
    guide_daily = Decimal(0)
    if hire_guide:
        guide_stats = Guide.objects.filter(agency__city=city).aggregate(
            low=Min('price_per_day'), mid=Avg('price_per_day'), high=Max('price_per_day')
        )
        guide_daily = Decimal(guide_stats[stay_tier] or 0)

    
    stay_total = stay_daily * d
    food_total = food_daily * 3 * d
    guide_total = guide_daily * d
    
    grand_total = stay_total + food_total + guide_total + transport_total + attraction_cost

    return {
        'total': grand_total.quantize(Decimal('1.')),
        'breakdown': {
            'Accommodation': stay_total.quantize(Decimal('1.')),
            'Food & Dining': food_total.quantize(Decimal('1.')),
            'Transportation': transport_total.quantize(Decimal('1.')),
            'Guide Services': guide_total.quantize(Decimal('1.')),
            'Entry Fees': attraction_cost.quantize(Decimal('1.'))
        }
    }