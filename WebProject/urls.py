from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('schedules/', include('schedules.urls')),
    path('', include('mainpage.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('schedules/', include('schedules.urls')),
]
