from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from shop.models import Contact
from django.contrib.auth import authenticate, login as dj_login, logout
from datetime import date
from django.contrib.auth.models import User



def home(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact_date = date.today()
        contact = Contact(contact_name=name, email=email, phone=phone, message=message, contact_date=contact_date)
        contact.save()

    return render(request, 'home/home.html')