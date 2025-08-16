from django.db import models
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    # image url ?
    @property
    def image_url(self):
        if self.image:
            return f"/media/{self.image}"
        return None

    
    def get_edit_url(self):
        return reverse('courses.edit', args=[self.id])

    def get_show_url(self):
        return reverse('courses.show', args=[self.id])

    def get_delete_url(self):
        return reverse('courses.delete', args=[self.id])


    @classmethod
    def get_all_courses(cls):
        return cls.objects.all().order_by('id')