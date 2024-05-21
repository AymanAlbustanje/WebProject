from django.urls import path
from . import views

urlpatterns = [
path('', views.schedules, name= 'schedule_page')

]