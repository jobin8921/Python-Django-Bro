from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
# Create your views here.

def logout(request):
    authlogout(request)              #Remove the authenticated user's ID from the request and flush their session data.
    return redirect('list')


def login(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('list')
        else:
            error_message='invalid credentials'
    
    return render(request,'users/login.html')


def signup(request):
    user=None
    error_message = None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message=str(e)

    return render(request,'users/create.html',{'user':user,'error_message':error_message})