from django import forms
from departments.models import Department

class DepartmentForm(forms.Form):

    name = forms.CharField(max_length=255, required=True)

    description = forms.CharField(widget=forms.Textarea, required=False)

    #validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if Department.objects.filter(name=name).exists():
            raise forms.ValidationError("Department with this name already exists")
        return name