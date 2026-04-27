from django.urls import path
from . import views




urlpatterns = [
    path('',                    views.hotel_list,         name='hotel_list'),
    path('<int:pk>/',           views.hotel_detail,       name='hotel_detail'),
    path('city/<int:city_id>/', views.hotel_list_by_city, name='hotel_list_by_city'),
    path('room/<int:room_id>/book/', views.book_room, name='book_room'),
]