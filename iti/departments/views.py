from django.shortcuts import render, redirect
from django.http import HttpResponse
from departments.forms import DepartmentForm
from departments.models import Department

# Create your views here.


def create_department(request):

    form = DepartmentForm()

    if request.method == 'POST':

        form = DepartmentForm(request.POST)

        if form.is_valid():

            department = Department.objects.create(**form.cleaned_data)

            return redirect('departments.all')

    return render(request, 'departments/create.html', context={'form': form})





def get_all_departments(request):

    # departments = Department.objects.all()
    departments = Department.get_all()

    return render(request, 'departments/index.html', 
    context={'departments': departments})

