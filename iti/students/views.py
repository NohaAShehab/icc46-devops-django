from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from django.shortcuts import get_object_or_404

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
    return render(request, 'students/staticIndex.html', 
    context={'students': students})


# django template language ==> jinja2
# provide a way to render the template with the data
# {{ }} ==> jinja2 syntax used to print the data
# {% %} ==> django template language syntax used to parse expressions
# if condition, for loop, etc.



"""
( I need to get all students from the database )
so I need to use Student model to get all students 

models provides a way to interact with the database
via functions  --> to deal with objects ?
1- need to get all students ::: Student.objects.all() "select * from students;"
# all query set of objects 

2- need to get a student by id ::: 
Student.objects.get(id=1) "select * from students where id=1;"
get return with one 

3- filter students by name ::: 
Student.objects.filter(name="John") "select * from students where name='John';"
filter return with list of objects 


"""

def all_students(request):
    # 1- get all students from the database
    students = Student.objects.all()
    # 2- send the data to the template
    return render(request, 'students/index.html', context={'students': students})



def show_student(request, id):


    """
    if you want to get a student by id  if object not found 404 error will be raised
    use get_object_or_404 function 
    """
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/show.html', 
    context={'student': student})
   
