from django.urls import path
from . import views

urlpatterns = [
    path('attractions/', views.attraction_list, name='attraction_list'),
    path('attractions/<int:pk>/', views.attraction_detail, name='attraction_detail'),
]