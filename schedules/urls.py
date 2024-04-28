from django.urls import path
from . import views

urlpatterns = [
path('', views.schedules, name= 'schedules page')

]