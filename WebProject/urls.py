from django.contrib import admin
from django.urls import path, include
from userauth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('schedules/', include('schedules.urls')),
    path('', include('mainpage.urls')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
