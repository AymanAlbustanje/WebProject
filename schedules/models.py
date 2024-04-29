from django.db import models
from courses.models import Course

class Schedule(models.Model):
    days = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
