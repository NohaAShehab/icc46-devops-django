from django.db import models

from django.shortcuts import reverse

# Create your models here.

"""
Model class should have all the logic related to the model
--> urls,
--> conditions applied on data retrieval  

"""


class Department(models.Model):

    name = models.CharField(max_length=255)

    # null=True means that the field is optional in the database 
    # if need field to optional in forms , admin or forms created by django 
    # you need to add property blank=True
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def show_url(self):
        return reverse('departments.show', args=[self.id])

    # get all objects from model ??
    @classmethod
    def get_all(cls):
        # order data, exclude some fields , do any operation. 
        return cls.objects.all()

    # define relation between departments and students


    
