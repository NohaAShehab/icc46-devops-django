from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View

from courses.forms import CourseForm

from courses.models import Course

from django.views.generic import (CreateView, DetailView, ListView, 
UpdateView, DetailView, DeleteView)


# Create your views here.


"""using class based views  """
# class based views

class CourseCreateView(View):
    
    def get(self, request):
        form = CourseForm()
        return render(request, 'courses/create.html', context={'form': form})


    def post(self, request):
        # when need to upload files in the form ??
        # in form.html enctype="multipart/form-data" 

        # you can get the file information ? request.FILES

        print(request.POST)
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('courses.index')

        return render(request, 'courses/create.html', context={'form': form})



class CoursesView(View):
    def get(self, request):
        courses = Course.get_all_courses()
        return render(request, 'courses/index.html', context={'courses': courses})



""" using generic views  """

class CourseGenericCreateView(CreateView):
    # model = Course 
    form_class = CourseForm  # form --> model form , django knows the model that will be used to save data 
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses.index')


class CourseGenericEditView(UpdateView):
    model = Course 
    form_class = CourseForm 
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('courses.index')

    # assume in url parameter is the pk ??




class CourseShowView(DetailView):
    model = Course 
    template_name = 'courses/show.html'
    # default context object name is object 
    context_object_name = 'course'



class CourseDeleteView(DeleteView):
    model = Course 
    template_name = 'courses/delete.html'  # confirm you want to delete ??
    success_url = reverse_lazy('courses.index')

    # define method to delete object and its related media ? 

    # or use package django-cleanup 

