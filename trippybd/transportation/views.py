from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Transportation
from cities.models import City # Assuming your city model is here

# Fixed the spelling of the function name
def transportation_list(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    transport_options = city.transportations.all()
    
    context = {
        'city': city,
        'transport_options': transport_options
    }
    # Make sure the template name here matches your actual file name
    return render(request, 'transportation/transportaion_list.html', context)