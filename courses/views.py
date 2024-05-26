from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from users.models import Student
from django.contrib import messages

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

    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        courses = filter_courses_by_prerequisites(courses, student)
    
    return render(request, 'courses/courses_list.html', {'courses': courses})

def filter_courses_by_prerequisites(courses, student):
    eligible_courses = []
    for course in courses:
        prerequisites = course.prerequisites.all()
        if all(prerequisite in student.completed_courses.all() for prerequisite in prerequisites):
            eligible_courses.append(course)
    return eligible_courses

@login_required
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    student, created = Student.objects.get_or_create(user=request.user)
    
    # Get the schedules of the new course
    new_course_schedules = course.schedules.all()
    
    # Check for schedule conflicts with already enrolled courses
    if Enrollment.objects.filter(student=student).exists():
        for enrollment in Enrollment.objects.filter(student=student):
            for enrolled_schedule in enrollment.course.schedules.all():
                for new_schedule in new_course_schedules:
                    if (enrolled_schedule.days == new_schedule.days and
                        not (new_schedule.end_time <= enrolled_schedule.start_time or new_schedule.start_time >= enrolled_schedule.end_time)):
                        # Redirect or return error message for schedule conflict
                        return redirect('course_detail', course_id=course_id)
    
    # Check other enrollment conditions (e.g., capacity)
    if Enrollment.objects.filter(student=student, course=course).exists():
        return redirect('course_detail', course_id=course_id)
    if course.enrollment_count >= course.capacity:
        return redirect('course_detail', course_id=course_id)
    
    # Create enrollment if no conflicts and conditions are met
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
        enrollment = Enrollment.objects.filter(student=request.user.student, course_id=course_id).first()
        if enrollment:
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

@login_required
def all_courses(request):
    student = request.user.student
    courses = Course.objects.all()
    eligible_courses = filter_courses_by_prerequisites(courses, student)
    
    return render(request, 'courses/all_courses.html', {'courses': eligible_courses})

@login_required
def mark_completed(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(Student, user=request.user)
    student.completed_courses.add(course)
    student.save()
    return redirect('course_detail', course_id=course_id)

def undo_mark_completed(request, course_id):
    if request.method == 'POST':
        # Get the course object
        course = Course.objects.get(pk=course_id)
        
        # Remove the course from completed courses for the current student
        if request.user.is_authenticated and hasattr(request.user, 'student'):
            student = request.user.student
            student.completed_courses.remove(course)
        
        # Redirect to the course detail page
        return redirect('course_detail', course_id=course_id)
    
def course_reports(request):
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    average_enrollments_per_course = total_enrollments / total_courses if total_courses > 0 else 0

    return render(request, 'courses/course_reports.html', {
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'average_enrollments_per_course': average_enrollments_per_course,
    })