from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        
        else:
            messages.success(request,"there was an error logging in,try again")
            return redirect('login')
        
    else:
        return render(request, 'members/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('mainpage')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"success!!")
            return redirect('mainpage')
        else:
            messages.success(request,"there was an error registering account,try again")
            return render(request, 'members/register.html')
    else:
        return render(request, 'members/register.html',{'form':form})

