from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_myaccount, name='myaccount'), # Event page# Form submitting function
]