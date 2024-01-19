from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige vers 'dashboard'
        else:
            return HttpResponse("Nom d'utilisateur ou mot de passe invalide.")
    return render(request, 'registration/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
