from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', include('analytics.urls')),
    path('', include('courses_management.urls')),
    # path('schedule_management', include('schedule_management.urls')),
    # path('user_authentication', include('user_authentication.urls')),
]
