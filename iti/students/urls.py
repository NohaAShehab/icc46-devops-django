
from django.urls import path
from students.views import (create_via_form, students_list, all_students, 
show_student, delete_student, create_student, create_via_form, edit_student)

urlpatterns = [
    path('list', students_list, name='students.list'),
    path('all', all_students, name='students.index'),
    path('show/<int:id>', show_student, name='students.show'),
    path('delete/<int:id>', delete_student, name='students.delete'),
    path('create', create_student, name='students.create'),
    path('form/create', create_via_form, name='students.createByForm'), 
    path('edit/<int:id>', edit_student, name='students.edit')
]
