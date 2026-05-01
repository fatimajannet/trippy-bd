from django.urls import path
from . import views

urlpatterns = [
    # This dynamic path handles all 5 categories using 'model_name'
    path('add/<str:model_name>/<int:object_id>/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]