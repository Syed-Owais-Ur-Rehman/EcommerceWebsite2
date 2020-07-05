from django.shortcuts import render
# from .models import --model--


# For Product objects to show use the following code
# ctrl+shift+p > Preferences: Configure Language Specific Settings > Python
# "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django",
#     ]


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def contact(request):
    return HttpResponse('This is the Contact Page')

def login(request):
    return HttpResponse('this is the Login Page')

def checkout(request):
    return HttpResponse('we are Checkout')

def search(request):
    return HttpResponse('we are Search')

def tracker(request):
    return HttpResponse('we are Tracker')

def productview(request):
    return HttpResponse('we are Product View')