
from django.urls import path
from students.views import students_list

urlpatterns = [
    path('list', students_list, name='students.list')
]
