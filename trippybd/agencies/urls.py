from django.urls import path
from . import views

urlpatterns = [
    path('<int:agency_id>/', views.agency_detail, name='agency_detail'),
    path('hire/<int:guide_id>/', views.hire_guide, name='hire_guide'),
    path('', views.agency_list, name='agency_list'), 
    path('hire/success/<int:hire_id>/', views.hire_success, name='hire_success'),
]