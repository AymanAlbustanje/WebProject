from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    # Your existing fields
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    # New field for one-to-one relationship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
