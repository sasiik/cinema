from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_myaccount, name='myaccount'), # User account 
    path('delete_event/', views.delete_item, name='delete_item') # Event page# Form submitting function
]