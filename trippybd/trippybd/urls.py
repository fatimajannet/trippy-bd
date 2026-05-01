"""
URL configuration for trippybd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from cities import views  

urlpatterns = [
    path('admin/',       admin.site.urls),
    path('accounts/',    include('accounts.urls')),
    path('cities/',      include('cities.urls')), 
    path('attractions/', include('attractions.urls')),
    path('hotels/',      include('hotels.urls')),       # ✅ fixed prefix
    path('restaurants/', include('restaurants.urls')),  # ✅ fixed prefix
    path('',             views.home, name='home'),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('cities/',      include(('cities.urls', 'cities'), namespace='cities')), 
    path('travel-history/', include(('travel_history.urls', 'travel_history'), namespace='travel_history')),
    path('agencies/', include('agencies.urls')),
    path('transportation/', include('transportation.urls')),
    path('budget/', include('budget.urls')),
    path('reviews/', include('review.urls')),

]
from django.conf import settings
from django.conf.urls.static import static
