from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_page, name='event_page'),
    path('participate/', views.participate, name='participate'),
]