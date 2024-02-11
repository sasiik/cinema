from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def choice(request):
    return render(request, 'choose_seat.html')
