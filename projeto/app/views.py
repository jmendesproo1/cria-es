
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from .models import User
from django.db import IntegrityError

def home(request):
    return render(request, 'home.html')


def cadastro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error': 'Este e-mail já está em uso.'})
        
        try:
            user = User.objects.create_user(email=email, password=password)
            return redirect('home')  
        except IntegrityError:
            return render(request, 'cadastro.html', {'error': 'Erro ao criar o usuário. Tente novamente.'})
    
    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'E-mail ou senha incorretos.'})
    
    return render(request, 'login.html')
