import uuid
from django.db import models
from django.urls import reverse

class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=200)
    
    institution = models.CharField(max_length=200)

    start_year = models.IntegerField()

    course = models.CharField(max_length=200)

    face = models.ImageField(upload_to='students_face/', blank=True) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': str(self.pk)})

