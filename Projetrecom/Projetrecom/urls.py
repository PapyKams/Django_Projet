"""
URL configuration for Projetrecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from appBdd.views import login_view, dashboard_view
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static  # Importation corrigée

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('dashboard/', dashboard_view, name='dashboard'),
    path("__debug__/", include("debug_toolbar.urls")),

    # ... autres URLs ...
]

urlpatterns += [
    path('', RedirectView.as_view(url='/accounts/login/'), name='root'),
]

# Ajoutez ceci uniquement si DEBUG est True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
