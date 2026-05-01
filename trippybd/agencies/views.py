from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, ExpressionWrapper, DateField
from datetime import timedelta
from .models import Agency, Guide, GuideHire 
from django.contrib.contenttypes.models import ContentType
from review.models import Review


def agency_detail(request, agency_id):
    agency = get_object_or_404(Agency, pk=agency_id)
    guides = agency.guides.all()

    agency_type = ContentType.objects.get_for_model(agency)
    reviews = Review.objects.filter(content_type=agency_type, object_id=agency.id)

    return render(request, 'agencies/agency_detail.html', {'agency': agency, 'guides': guides, 'reviews': reviews})


@login_required
def hire_guide(request, guide_id):
    guide = get_object_or_404(Guide, pk=guide_id)
    
    if request.method == 'POST':
        hire_date_str = request.POST.get('hire_date')
        days = int(request.POST.get('days'))
        
        # Convert the string from the form into a Python Date object
        from datetime import datetime
        requested_date = datetime.strptime(hire_date_str, '%Y-%m-%d').date()

        # CHECK FOR CONFLICTS:
        # We look for any existing booking where the requested date falls 
        # between the start_date and the end_date (start + days).
        
        # Logic: Existing Start Date <= Requested Date < (Existing Start Date + Existing Days)
        conflicting_bookings = GuideHire.objects.filter(
            guide=guide,
            hire_date__lte=requested_date  # Previous booking started on or before requested date
        )

        for booking in conflicting_bookings:
            # Calculate when that specific booking ends
            end_date = booking.hire_date + timedelta(days=booking.days)
            
            if requested_date < end_date:
                messages.error(request, f"Sorry, {guide.g_name} is busy from {booking.hire_date} to {end_date - timedelta(days=1)}. Please choose another date.")
                return render(request, 'agencies/hire_form.html', {'guide': guide})

        # If no conflict was found, proceed to hire
        calculated_cost = guide.price_per_day * days
        new_hire = GuideHire.objects.create(
            user=request.user,
            guide=guide,
            hire_date=requested_date,
            days=days,
            total_cost=calculated_cost,
            status='Pending'
        )
        
        messages.success(request, f"Hiring request for {guide.g_name} sent!")
        return redirect('hire_success', hire_id=new_hire.pk)

    return render(request, 'agencies/hire_form.html', {'guide': guide})

from cities.models import City # Import your City model

def agency_list(request):
    agencies = Agency.objects.all()
    cities = City.objects.all() # You MUST fetch the cities here
    return render(request, 'agencies/agency_list.html', {
        'agencies': agencies,
        'cities': cities # Pass them to the template
    })

# agencies/views.py
def hire_success(request, hire_id):
    hire = get_object_or_404(GuideHire, pk=hire_id, user=request.user)
    return render(request, 'agencies/hire_success.html', {'hire': hire})

# Update your existing hire_guide view:
    if request.method == 'POST':
        # ... your existing logic ...
        new_hire = GuideHire.objects.create(...)
        return redirect('hire_success', hire_id=new_hire.pk)