from django.urls import path
from . import views

urlpatterns = [
    path('', views.choice, name='seat_choice')
]