from django.urls import path
from . import views

app_name = 'travel_history'

urlpatterns = [
    # 1. The main list page
    path('', views.TravelHistoryListView.as_view(), name='travel_history'),
    
    # 2. The "Mark as Visited" action (Used by your Wishlist button)
    # We map 'add_to_history' to your 'mark_visited' function in views.py
    path('add/<int:city_id>/', views.mark_visited, name='add_to_history'),
    
    # 3. The remove action
    path('remove/<int:entry_id>/', views.remove_visited, name='remove_visited'),

    path('toggle/<int:city_id>/', views.toggle_visited, name='toggle_visited'),
]
