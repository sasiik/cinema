from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.display_seats, name='display_seats') # Choose seat url
]