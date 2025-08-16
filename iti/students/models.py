from django.db import models
from django.shortcuts import reverse
from departments.models import Department
# Create your models here.


"""
I need to connect to the database 
1- model is a python class that represents a table in the database
it is normal  python class inheriting from models.Model

DB table (name, id , age, email , gender, birth_date)

ceate table students(
    id int primary key auto_increment,
    name varchar(255),
    age int,
    email varchar(255),
    gender varchar(255) enum('male', 'female'),
    birth_date date
)

2- migration ??

# to create migration files 
# python manage.py makemigrations
# when you run this command, django check the models files in all installed apps for changes
# if there are any changes, it will create a migration file for each model that has changes
# the migration file is a file that contains the changes to be applied to the database
# the migration file is stored in the migrations folder of the app
# the migration file is named like this: 0001_initial.py
# the number is the order of the migration file
# the initial is the name of the migration file


# to apply the migration files to the database
# python manage.py migrate
this will create table students_student in db ??
students ==> name of the app
student ==> name of the model

### check this 
    when you create table in sql --> by default fields are null  

    when you create table in django --> by default fields are not null
    if you want to make a field nullable, you need to add null=True
"""





class Student(models.Model):
    # use model to define the fields of the table
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(default=10)
    email = models.EmailField(max_length=255, null=True, unique=True)
    gender = models.CharField(max_length=255, choices=[('male', 'Male'), ('female', 'Female')], 
    null=True)
    birth_date = models.DateField(null=True)
    # I need to add field represent created_at and updated_at
    created_at = models.DateTimeField(auto_now_add=True, null=True) # this value will be automatically set when the object is created
    updated_at = models.DateTimeField(auto_now=True, null=True) # this value will be automatically set when the object is updated


    # define relation between students and departments

    # if you want to get students related to a department ??
    # backword relation ??
    # student. department is an object  ==> get all students related to a department 

    # student.department.students_set.all()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
     null=True, related_name='students')
    
    def __str__(self):
        return f"{self.name}"

    # define the show_url --> read only value ??
    @property
    def show_url(self):
        return reverse('students.show', args=[self.id])
    
    
    @property
    def delete_url(self):
        return reverse('students.delete', args=[self.id])

    

    





 
"""
we need to try the table in admin panel
we need to create a super user
python manage.py createsuperuser
/





"""

