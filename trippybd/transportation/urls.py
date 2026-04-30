from django.urls import path
from . import views

urlpatterns = [
    # Add <int:city_id>/ so the view gets the ID it needs
    path('city/<int:city_id>/', views.transportation_list, name='transportation_list'),
]