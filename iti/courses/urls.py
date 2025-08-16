from django.urls import path

from courses.views import (CourseCreateView, CoursesView, CourseGenericCreateView, 
CourseGenericEditView, CourseShowView, CourseDeleteView)

urlpatterns = [

    # path('create', CourseCreateView.as_view(), name='courses.create'),
    path('create', CourseGenericCreateView.as_view(), name='courses.create'),
    path('all', CoursesView.as_view(), name='courses.index'),
    
    path('edit/<int:pk>', CourseGenericEditView.as_view(), name='courses.edit'),

    path('<int:pk>', CourseShowView.as_view(), name='courses.show'),


    path('delete/<int:pk>', CourseDeleteView.as_view(), name='courses.delete'),
    

]

