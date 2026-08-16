from django.shortcuts import render
from django.http import HttpResponse

def authapp_home(request):
    return HttpResponse("Welcome to the AuthApp Home Page!")

# Create your views here.
