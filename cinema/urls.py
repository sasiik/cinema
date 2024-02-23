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
from django.urls import path, include
from main import views as home_views
import debug_toolbar

urlpatterns = [
    path('', home_views.redirect_to_home),
    path('admin/', admin.site.urls, name='admin'),
    path('home/', include('main.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('event/', include('event.urls')),
    path('seats/', include('seats.urls')),
    path('user/', include('user.urls')),
]
