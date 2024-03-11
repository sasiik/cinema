from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'), # Signup
    path('login/', views.userlogin, name='login'), # Login
    path('logout/', views.userlogout, name='logout') # Log out
]