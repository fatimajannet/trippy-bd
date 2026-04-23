from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_view, name='wishlist'),
    path('add/<int:city_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('remove-city/<int:city_id>/', views.remove_city_from_wishlist, name='remove_city_from_wishlist'),
    path('api/check/<int:city_id>/', views.check_in_wishlist, name='check_in_wishlist'),
]