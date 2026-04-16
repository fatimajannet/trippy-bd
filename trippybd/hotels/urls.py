# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:city_id>/hotels/', views.hotel_list, name='hotel_list'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
]