from django.db import models
from users.models import Student

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    instructor_name = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField('self', blank=True)
    capacity = models.PositiveIntegerField()

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
