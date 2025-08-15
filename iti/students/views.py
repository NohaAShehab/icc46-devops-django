from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def students_list(request):
#     # return HttpResponse("students_list")
#     return render(request, 'students/index.html')



# send data to the template
def students_list(request):
    students = [
        {'name': 'John', 'age': 20, 'id': 1},
        {'name': 'Jane', 'age': 21, 'id': 2},
        {'name': 'Jim', 'age': 22, 'id': 3},
    ]
    return render(request, 'students/index.html', 
    context={'students': students})


# django template language ==> jinja2
# provide a way to render the template with the data
# {{ }} ==> jinja2 syntax used to print the data
# {% %} ==> django template language syntax used to parse expressions
# if condition, for loop, etc.


