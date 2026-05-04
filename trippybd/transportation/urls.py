from django.urls import path
from . import views

urlpatterns = [
    path('city/<int:city_id>/', views.transportation_list, name='transportation_list'),
]