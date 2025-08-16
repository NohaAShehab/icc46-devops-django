from django import forms
from students.models import Student
import re

class StudentForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)
    birth_date = forms.DateField(required=True)


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
    