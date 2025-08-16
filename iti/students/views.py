from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from students.forms import StudentForm, StudentModelForm
from students.models import Student




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

4- create a new student ::: 
student = Student()
student.name = "new"
student.email = "newstudent@gmail.com"
student.age = 3
student.gender = "male"
student.birth_date = "2025-08-08"
student.save()



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

    print(f"student, {student.department}, {type(student.department)}")

    return render(request, 'students/show.html', 
    context={'student': student})




def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    # django provides a way to delete an object ??
    # delete function 
    student.delete()  # this will delete the object from the database
    ## I need to redirect to the index page 
    return redirect('students.index')  # accept url name 



def create_student(request):
    # I need to print the request variable 
    print(request)
    """
    You need aform -> to get the data from the user 
    
    """

    # I need to decide what to do if the request method is post /?


    if request.method == 'POST':
        print(request.POST)
        """
        <QueryDict: {'csrfmiddlewaretoken': ['PLh701PEP2qEjeAhejdXXuMeAHI2S5riFybpZ1dBswwSsVAdnuuCA03vxi0Tmnr6'],
        'name': ['new'], 
        'email': ['newstudent@gmail.com'], 
        'age': ['3'], 
        'gender': ['male'], 
        'birth_date': ['2025-08-08']}>
        """
        # I need to get the data 
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')

        # check if eamil exists  
        if Student.objects.filter(email=email).exists():
            # I need to show a message to the user 
            return render(request, 'students/create.html', context={'message': 'Email already exists'})
        else:
            # I need to create a new student object 
            student = Student()
            student.name = name
            student.email = email
            student.age = age
            student.gender = gender
        # I need to create a new student object 
        student = Student()
        student.name = name
        student.email = email
        student.age = age
        student.gender = gender
        student.birth_date = birth_date
        student.save() # save object to the database
        print(student.id)

        # I need to redirect to the index page 
        # return redirect('students.index')
        return redirect('students.show', id=student.id)




    return render(request, 'students/create.html')




def create_via_form(request):
    # I need to create a new student object 
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # create the student ?? request.POST, form.cleaned_data ??
            print(form.cleaned_data)
            # you must pass the department  as object not the id 
            student = Student.objects.create(**form.cleaned_data)
            
            return redirect('students.show', id=student.id)

    return render(request, 'students/createByForm.html', 
    context={'form': form})



def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    form = StudentModelForm(instance=student)

    if request.method == 'POST':

        form = StudentModelForm(request.POST, instance=student)

        if form.is_valid(): 

            form.save()  # use form object to save the data 

            return redirect('students.show', id=student.id)
            
    return render(request, 'students/edit.html', context={'form': form})