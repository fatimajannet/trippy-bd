from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.attraction_list,         name='attraction_list'),
    path('<int:pk>/',           views.attraction_detail,       name='attraction_detail'),
    path('city/<int:city_id>/', views.attraction_list_by_city, name='attraction_list_by_city'),
]