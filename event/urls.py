from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.display_event, name='event_page'), # Event page
    path('participate/<int:event_id>', views.participate, name='participate'), # Form submitting function
]