from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_planner, name='budget_planner'),
    path('details/<int:city_id>/<str:tier>/', views.plan_details, name='plan_details'),
]