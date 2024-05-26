from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Enrollment
from schedules.models import Schedule

@login_required
def schedules(request):
    student = request.user.student
    enrollments = Enrollment.objects.filter(student=student).select_related('course')
    courses = [enrollment.course for enrollment in enrollments]
    schedules = Schedule.objects.filter(course__in=courses).order_by('days', 'start_time')
    return render(request, 'schedules/schedule_page.html', {'schedules': schedules})
