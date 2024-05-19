from django.urls import path
from . import views

urlpatterns = [
path('courses/', views.Course, name= 'courses page'),
path('courses', views.Course, name= 'courses page'),
path('search/', views.course_search_view, name='course_search'),
path('search', views.course_search_view, name='course_search'),
path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
]