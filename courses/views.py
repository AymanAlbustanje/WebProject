# courses/views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.http import JsonResponse

from users.models import Student
from .models import Course, Enrollment

def course_search_view(request):
    query = request.GET.get('q')
    print("Query:", query)  # Debug statement
    if query:
        courses = Course.objects.filter(
            Q(course_code__icontains=query) |
            Q(course_name__icontains=query) |
            Q(instructor_name__icontains=query)
        )
        print("Filtered Courses:", courses)  # Debug statement
    else:
        courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        # Redirect to the login page if the user is not authenticated
        return redirect('login')
    
    # Retrieve or create the associated Student object for the current user
    student, created = Student.objects.get_or_create(user=request.user)

    # Check if the student is already enrolled in the course
    if Enrollment.objects.filter(student=student, course=course).exists():
        # Redirect to a page indicating that the student is already enrolled
        return redirect('course_detail', course_id=course_id)

    # If not already enrolled, create an enrollment record
    enrollment = Enrollment.objects.create(student=student, course=course)
    
    # Increment the enrollment count of the course
    course.enrollment_count += 1
    course.save()

    # Redirect to a page indicating successful enrollment
    return redirect('course_detail', course_id=course_id)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})
