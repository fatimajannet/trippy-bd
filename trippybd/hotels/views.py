from django.shortcuts import render, get_object_or_404
from .models import Hotel
from cities.models import City
from django.contrib.contenttypes.models import ContentType
from review.models import Review


def hotel_list(request):
    hotels = Hotel.objects.select_related('city').all()
    cities = City.objects.all()
    return render(request, 'hotels/hotel_list.html', {
        'hotels': hotels,
        'cities': cities,
    })

def hotel_list_by_city(request, city_id):
    city   = get_object_or_404(City, pk=city_id)
    hotels = Hotel.objects.filter(city=city).select_related('city')
    cities = City.objects.all()
    return render(request, 'hotels/hotel_list.html', {
        'hotels':        hotels,
        'selected_city': city,
        'cities':        cities,
    })

def hotel_detail(request, pk):
    hotel = get_object_or_404(
        Hotel.objects.select_related('city').prefetch_related('amenities', 'rooms'), 
        pk=pk
    )
    
    hotel_type = ContentType.objects.get_for_model(hotel)

    reviews = Review.objects.filter(content_type=hotel_type, object_id=hotel.id)

    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel, 'reviews': reviews})





import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from datetime import datetime, timedelta

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    
    # 1. Fetch all busy dates for this room
    existing_bookings = Booking.objects.filter(room=room)
    booked_dates = []
    for b in existing_bookings:
        curr = b.check_in
        # We use < b.check_out so the checkout day remains 'available' for a new check-in
        while curr < b.check_out:
            booked_dates.append(curr.strftime('%Y-%m-%d'))
            curr += timedelta(days=1)
    
    booked_dates_json = json.dumps(booked_dates)

    if request.method == 'POST':
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        
        try:
            d1 = datetime.strptime(check_in_str, '%Y-%m-%d').date()
            d2 = datetime.strptime(check_out_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, "Invalid date format.")
            return redirect('book_room', room_id=room.id)

        # 2. Logic: No same-day check-in/out
        delta = d2 - d1
        if delta.days < 1:
            messages.error(request, "Minimum stay is 1 night. Same-day checkout is not permitted.")
            return render(request, 'hotels/booking_form.html', {'room': room, 'booked_dates_json': booked_dates_json})

        # 3. Logic: Overlap Check
        # Allows checkout day of one guest to be the checkin day of the next
        overlap = Booking.objects.filter(
            room=room,
            check_in__lt=d2, # Existing start is before new end
            check_out__gt=d1  # Existing end is after new start
        ).exists()

        if overlap:
            messages.error(request, "This room is already occupied during your selected dates.")
            return render(request, 'hotels/booking_form.html', {'room': room, 'booked_dates_json': booked_dates_json})

        # 4. Save Booking
        Booking.objects.create(
            user=request.user,
            room=room,
            check_in=d1,
            check_out=d2,
            total_price=room.r_price * delta.days
        )
        messages.success(request, f"Successfully booked {room.r_type} at {room.hotel.name}!")
        return redirect('dashboard')

    return render(request, 'hotels/booking_form.html', {
        'room': room, 
        'booked_dates_json': booked_dates_json
    })