from django.urls import path
from . import views

urlpatterns = [
path('courses', views.all_courses, name='all_courses'),
path('courses/', views.all_courses, name='all_courses'),
path('search/', views.course_search_view, name='course_search'),
path('search', views.course_search_view, name='course_search'),
path('<int:course_id>/', views.course_detail, name='course_detail'),
path('<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
path('courses/<int:course_id>/drop/', views.drop_course, name='drop_course'),
path('schedule/', views.schedule_page, name='schedule_page'),
path('<int:course_id>/mark_completed/', views.mark_completed, name='mark_completed'),
path('<int:course_id>/undo_mark_completed/', views.undo_mark_completed, name='undo_mark_completed'),
path('reports/', views.course_reports, name='course_reports'),
]