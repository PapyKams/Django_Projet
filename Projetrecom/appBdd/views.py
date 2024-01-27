# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import prospect # Assurez-vous que le modèle prospect est importé

  
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

def dashboard(request):
    prospects = prospect.objects.all()  # Assurez-vous que cette requête récupère les données.
    return render(request, 'dashboard.html', {'prospects': prospects})


@login_required
def dashboard_view(request):
    donnees = prospect.objects.all()  # Assurez-vous que c'est le bon modèle
    return render(request, 'dashboard.html', {'donnees': donnees})

