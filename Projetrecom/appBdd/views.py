# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Prospect # Assurez-vous que le modèle Prospect est importé

  
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Assurez-vous que 'dashboard' est le nom correct de l'URL
        else:
            # Message d'erreur si l'authentification échoue
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')


@login_required
def dashboard_view(request):
    donnees = Prospect.objects.all()  # Assurez-vous que c'est le bon modèle
    return render(request, 'dashboard.html', {'donnees': donnees})

