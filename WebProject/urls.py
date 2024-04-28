from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('schedules/', include('schedules.urls')),
]
