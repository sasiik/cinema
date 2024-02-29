from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/home')
            else:
                messages.error(request, "Wrong username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def userlogout(request):
    logout(request)
    return redirect('/home')


def retrieve_user_data(request):
    current_user = CustomUser.objects.filter(user=request.user)
    return current_user