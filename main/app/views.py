from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import User



# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, 'app/home.html', {'users':users})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credential')
            return redirect('home')

        
    return render(request, 'app/userLogin.html')



def userRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('userRegister')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('userRegister')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        
        login(request, user)
        return redirect('home')


    return render(request, 'app/userRegister.html')



def userLogout(request):
    logout(request)
    return redirect('home')


