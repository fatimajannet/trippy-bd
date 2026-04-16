from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})