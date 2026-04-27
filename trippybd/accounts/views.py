from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm
from agencies.models import GuideHire
from hotels.models import Booking
from wishlist.models import Wishlist    # If you want to show saved items

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.fname}! Account created successfully.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.fname}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login')



@login_required
def dashboard_view(request):
    # 1. Fetch Guide Hires
    hired_guides = GuideHire.objects.filter(user=request.user).order_by('-hire_date')
    
    # 2. FIX THIS LINE (Line 57): Change RoomBooking to Booking
    hotel_bookings = Booking.objects.filter(user=request.user).order_by('-check_in')
    
    # 3. Fetch Wishlist
    wishlist_items = Wishlist.objects.filter(user=request.user)

    context = {
        'user': request.user,
        'hired_guides': hired_guides,
        'hotel_bookings': hotel_bookings,
        'wishlist_items': wishlist_items,
    }
    
    return render(request, 'accounts/dashboard.html', context)


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('dashboard')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})