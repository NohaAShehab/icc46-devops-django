from django.urls import path
from departments.views import create_department, get_all_departments

urlpatterns = [
    path('create', create_department, name='departments.create'),
    
    path('all', get_all_departments, name='departments.all'),
]