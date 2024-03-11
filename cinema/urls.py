"""
URL configuration for cinema project.

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
from django.shortcuts import redirect
from django.urls import path, include

def redirect_to_home(request):
    return redirect('home')

urlpatterns = [
    path('', redirect_to_home), # Home page is /hoome
    path('admin/', admin.site.urls, name='admin'),
    path('home/', include('main.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('event/', include('event.urls')), # Event page 
    path('seats/', include('seats.urls')), # Seats choice
    path('user/', include('user.urls')), # User pages (login, register, etc.)
]
