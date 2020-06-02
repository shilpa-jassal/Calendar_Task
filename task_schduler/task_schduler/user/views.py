from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.
def login(request):
    if request.session.has_key('is_logged'):
        return redirect('home')
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        count=User.objects.filter(email=email,password=password).count()
        if count >0:
            request.session.set_expiry(20)
            request.session['is_logged']=True
            return redirect('home')
        else:
            messages.error(request,'Invalid Email or Password')
            return redirect("login")
    return render(request,'user/login.html')

def signup(request):
    return render(request,'user/signup.html')

def register_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        obj=User(username=username,email=email,password=password)
        obj.save() 
        messages.success(request,'you are registered successfully...')
        return redirect('login')



def home(request):
    if request.session.has_key('is_logged'):

        return render(request,'user/home.html')
    return redirect('login')

def logout(request):
    print("i am here")
    del request.session['is_logged']
    return redirect('login')

