
from django.urls import path
from students.views import students_list, all_students, show_student, delete_student, create_student

urlpatterns = [
    path('list', students_list, name='students.list'),
    path('all', all_students, name='students.index'),
    path('show/<int:id>', show_student, name='students.show'),
    path('delete/<int:id>', delete_student, name='students.delete'),
    path('create', create_student, name='students.create')
]
