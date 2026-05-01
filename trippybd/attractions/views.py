from django.shortcuts import render, get_object_or_404
from .models import Attraction
from cities.models import City
from django.contrib.contenttypes.models import ContentType
from review.models import Review


def attraction_list(request):
    attractions = Attraction.objects.select_related('city').all()
    cities      = City.objects.all()
    return render(request, 'attractions/attraction_list.html', {
        'attractions': attractions,
        'cities':      cities,
    })

def attraction_list_by_city(request, city_id):
    city        = get_object_or_404(City, pk=city_id)
    attractions = city.attraction_set.select_related('city').all()
    cities      = City.objects.all()
    return render(request, 'attractions/attraction_list.html', {
        'attractions':   attractions,
        'selected_city': city,
        'cities':        cities,
    })

def attraction_detail(request, pk):
    attraction = get_object_or_404(
        Attraction.objects.select_related('city'), pk=pk
    )

    attr_type = ContentType.objects.get_for_model(attraction)
    reviews = Review.objects.filter(content_type=attr_type, object_id=attraction.id)

    return render(request, 'attractions/attraction_detail.html', {
        'attraction': attraction, 
    })