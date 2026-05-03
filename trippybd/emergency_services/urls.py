from django.urls import path
from . import views

app_name = 'emergency_services'

urlpatterns = [
    path('', views.emergency_list, name='list'),
]