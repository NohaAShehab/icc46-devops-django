
# I need form to create course? 

from django import forms


from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Course.objects.filter(name=name).exists():
            raise forms.ValidationError("Course with this name already exists")
        return name
    
    

# I need to add image field to the form ?