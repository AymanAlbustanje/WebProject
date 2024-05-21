# courses/views.py
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from users.models import Student

def course_search_view(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            Q(course_code__icontains=query) |
            Q(course_name__icontains=query) |
            Q(instructor_name__icontains=query)
        )
    else:
        courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    student, created = Student.objects.get_or_create(user=request.user)
    if Enrollment.objects.filter(student=student, course=course).exists():
        return redirect('course_detail', course_id=course_id)
    if course.enrollment_count >= course.capacity:
        return redirect('course_detail', course_id=course_id)
    Enrollment.objects.create(student=student, course=course)
    course.enrollment_count += 1
    course.save()
    return redirect('course_detail', course_id=course_id)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment_count = course.enrollments.count()
    schedules = course.schedules.all()
    enrolled = False
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        enrolled = Enrollment.objects.filter(course=course, student=request.user.student).exists()
    
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'enrollment_count': enrollment_count,
        'enrolled': enrolled,
        'schedules': schedules,
    })

@login_required
def drop_course(request, course_id):
    if request.method == 'POST':
        # Get the current user's enrollment for the specified course
        enrollment = Enrollment.objects.filter(student=request.user.student, course_id=course_id).first()
        if enrollment:
            # If the user is enrolled in the course, delete the enrollment
            enrollment.delete()
    return redirect('course_detail', course_id=course_id)

def schedule_page(request):
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        enrollments = Enrollment.objects.filter(student=student).select_related('course')
    else:
        enrollments = []
    
    return render(request, 'schedule_page.html', {
        'enrollments': enrollments,
    })

def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', {'courses': courses})