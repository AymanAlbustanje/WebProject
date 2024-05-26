from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    completed_courses = models.ManyToManyField('courses.Course', related_name='completed_by_students', blank=True)

    def __str__(self):
        return self.name
