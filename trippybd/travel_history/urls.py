from django.urls import path
from . import views

app_name = 'travel_history'

urlpatterns = [
    path('', views.TravelHistoryListView.as_view(), name='travel_history'),
    
    path('add/<int:city_id>/', views.mark_visited, name='add_to_history'),
    
    path('remove/<int:entry_id>/', views.remove_visited, name='remove_visited'),

    path('toggle/<int:city_id>/', views.toggle_visited, name='toggle_visited'),
]
