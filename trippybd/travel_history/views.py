import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from cities.models import City
from .models import TravelHistory
from wishlist.models import Wishlist 
from django.contrib.auth.decorators import login_required
from django.contrib import messages  



@login_required
def mark_visited(request, city_id):
    if request.method == 'POST':
        city = get_object_or_404(City, id=city_id)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        try:
            TravelHistory.objects.get_or_create(user=request.user, city=city)
            
            Wishlist.objects.filter(user=request.user, city=city).delete()

            if is_ajax:
                return JsonResponse({'status': 'success', 'city': city.name})
            return redirect('travel_history:travel_history')

        except Exception as e:
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            return redirect('travel_history:travel_history')

    return redirect('cities:city_list')

@method_decorator(login_required, name='dispatch')
class TravelHistoryListView(ListView):
    model = TravelHistory
    template_name = 'travel_history/travel_history.html'
    context_object_name = 'history_entries'
    paginate_by = 12

    def get_queryset(self):
        return TravelHistory.objects.filter(
            user=self.request.user
        ).select_related('city')


@login_required
def remove_visited(request, entry_id):
    """Allows user to remove a city from their travel history."""
    if request.method == 'POST':
        entry = get_object_or_404(TravelHistory, id=entry_id, user=request.user)
        city_name = entry.city.name
        entry.delete()
        messages.success(request, f'"{city_name}" removed from your travel history.')
    return redirect('travel_history:list')




@login_required
def toggle_visited(request, city_id):
    if request.method == 'POST':
        city = get_object_or_404(City, id=city_id)
        history_item = TravelHistory.objects.filter(user=request.user, city=city)
        
        if history_item.exists():
            history_item.delete()
            return JsonResponse({'status': 'success', 'is_visited': False})
        else:
            TravelHistory.objects.create(user=request.user, city=city)
            Wishlist.objects.filter(user=request.user, city=city).delete()
            return JsonResponse({'status': 'success', 'is_visited': True})
            
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def remove_visited(request, entry_id):
    if request.method == 'POST':
        entry = get_object_or_404(TravelHistory, id=entry_id, user=request.user)
        entry.delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
            
        messages.success(request, 'City removed from history.')
    return redirect('travel_history:travel_history')