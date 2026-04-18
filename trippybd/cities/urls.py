from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_list, name='city_list'),  # This will show the city list at '/cities/'
    path('<int:city_id>/', views.city_details, name='city_details'),  # Show city details at '/cities/{id}/'
]