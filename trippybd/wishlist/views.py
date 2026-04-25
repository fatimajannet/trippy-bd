from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from .models import Wishlist
from cities.models import City
from travel_history.models import TravelHistory

@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user).select_related('city')
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': items})

@login_required
def add_to_wishlist(request, city_id):
    if request.method != 'POST':
        return HttpResponseForbidden()
    
    city = get_object_or_404(City, id=city_id)
    
    # --- NEW SECURITY CHECK ---
    # Check if the city is already in the user's travel history
    is_visited = TravelHistory.objects.filter(user=request.user, city=city).exists()
    
    if is_visited:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'error',
                'message': 'You have already visited this city!',
                'in_wishlist': False
            }, status=400) # Sending a 400 error to indicate a bad request
        return redirect(request.META.get('HTTP_REFERER', '/'))
    # --------------------------

    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, city=city)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'created': created,
            'message': 'Added to wishlist' if created else 'Already in wishlist',
            'in_wishlist': True
        })
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_wishlist(request, wishlist_id):
    if request.method != 'POST':
        return HttpResponseForbidden()
    item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    item.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Removed from wishlist', 'in_wishlist': False})
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_city_from_wishlist(request, city_id):
    if request.method != 'POST':
        return HttpResponseForbidden()
    item = get_object_or_404(Wishlist, user=request.user, city_id=city_id)
    item.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Removed from wishlist', 'in_wishlist': False})
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def check_in_wishlist(request, city_id):
    in_wishlist = Wishlist.objects.filter(user=request.user, city_id=city_id).exists()
    return JsonResponse({'in_wishlist': in_wishlist})