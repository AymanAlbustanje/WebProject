from django.urls import path
from . import views

urlpatterns = [
path('', views.users, name= 'Users page')

]