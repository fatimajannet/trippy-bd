from django.shortcuts import render
from .models import EmergencyService

def emergency_list(request):
    
    services = EmergencyService.objects.select_related('city').all()
    
    return render(request, 'emergency_services/emergency_list.html', {
        'services': services
    })