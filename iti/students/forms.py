from django import forms
from students.models import Student
from departments.models import Department
import re

class StudentForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)

    age = forms.IntegerField(required=True)

    email = forms.EmailField(required=True)

    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)

    birth_date = forms.DateField(required=True)

    department= forms.ModelChoiceField(queryset=Department.objects.all(), required=True)


    # define validators for the form
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email



    def clean_name(self):
        # cleaned data  --> function that returns the cleaned data
        # in terms of --> remove the spaces
        name = self.cleaned_data.get('name')
        print(name)
        # name should be consists of characters and spaces 
        if not re.match(r'^[a-zA-Z\s]+$', name) or len(name) < 3:
            raise forms.ValidationError("Name must be consists of characters and spaces and at least 3 characters")
        return name
    


# class form --> based on model 

class StudentModelForm(forms.ModelForm):
    class Meta: 
        model = Student

        # take form fields from model class 
        fields = "__all__"

    def clean_email(self):

        print(self.instance, "here")
        # I need incase of update to ignore the email of the student ?
        email = self.cleaned_data.get('email')
        
        found = Student.objects.filter(email=email)  # list objects that match email 

        if self.instance.id is not None:  # edit existing student
            found = found.exclude(id=self.instance.id)

        if found.exists():
            raise forms.ValidationError("Email already exists")

       
        return email
    

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name) or len(name) < 3:
            raise forms.ValidationError("Name must be consists of characters and spaces and at least 3 characters")
        return name
    

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Age must be greater than 18")
        return age
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name) or len(name) < 3:
            raise forms.ValidationError("Name must be consists of characters and spaces and at least 3 characters")
        return name
    
 

    
    
