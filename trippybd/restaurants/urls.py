from django.urls import path
from . import views

urlpatterns = [
    path('',               views.restaurant_list,   name='restaurant_list'),
    path('<int:pk>/',      views.restaurant_detail, name='restaurant_detail'),
    path('city/<int:city_id>/', views.restaurant_list_by_city, name='restaurant_list_by_city'),
]