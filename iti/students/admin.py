from django.contrib import admin

# Register your models here.
# when you add them , it will be shown in the admin panel 

from students.models import Student

admin.site.register(Student)
