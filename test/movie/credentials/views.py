from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'this username already exists, try another username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'this email already exists,try another email id')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/credentials/login')

        else:
            messages.info(request, 'password dosent match')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            messages.success(request, f'{username}. You are now logged in.')
            auth_login(request,user)
            return redirect('/movieapp/home/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/credentials/login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/credentials/login')