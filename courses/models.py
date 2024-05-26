from django.db import models
from users.models import Student

class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    enrollment_count = models.PositiveIntegerField(default=0)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.name} enrolled in {self.course.course_name}'
