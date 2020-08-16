from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from math import ceil
from datetime import date
from django.contrib.auth.models import User


# For Product objects to show use the following code
# ctrl+shift+p > Preferences: Configure Language Specific Settings > Python
# "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django",
#     ]


# Create your views here.
# from django.http import 

def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    
    # params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products}
    #allprods = [[products, range(1,nslides), nslides],
    #            [products, range(1,nslides), nslides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods' : allprods}
    return render(request, 'shop/index.html', params)

def admin(request):
    messages.success(request, "You Have Logged In")
    return render(request, 'shop/admin.html')

def addform(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        category = request.POST.get('category', '')
        email = request.POST.get('email', '')
        price = request.POST.get('price', '')
        desc = request.POST.get('desc', '')
        image = request.FILES['image']
        pub_date = request.POST.get('date', '')
        addform = Product(product_name=name, email=email, price=price, desc=desc, image=image, category=category, pub_date=pub_date)
        addform.save()
    return render(request, 'shop/addform.html')

def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            dj_login(request, user)
            return redirect("/shop/admin")
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect("/shop/login")

    return render(request, 'shop/login.html')

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['psw']
        repassword = request.POST['psw-repeat']

        # Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect("/shop/success")

    # else:
    #     return HttpResponse("404 - Not Found")

    #check errors

    return render(request, 'shop/signup.html') 

def success(request):
    messages.success(request, "Your Account Has Been Successfully Created")
    return render(request, 'shop/success.html') 

def cart(request):
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods' : allprods}
    return render(request, 'shop/cart.html', params)



import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == 'POST':
        print('Data:', request.POST)
        order_email = request.POST['customeremail']
        fname = request.POST['fname']
        lname = request.POST['lname']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        country = request.POST['country']
        city = request.POST['city']
        phoneno = request.POST['phone']
        orderdate = date.today()
        totalprice = request.POST['totalprice']
        orderform = Customer(fname=name, lname=lname, address1=add1, address2= add2, email=order_email, country=country, city=city, phone=phoneno, totalprice=totalprice, order_date=orderdate)
        orderform.save()

        
        customer = stripe.Customer.create(
            email=email,
            name=fname + ' ' + lname
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=5000,
            # (totalprice*100)
            currency='usd',
            description='Customer Purchase'
            )

    return render(request, 'shop/checkout.html')

# def ch(request):
#     publishkey = settings.STRIPE_PUBLISHABLE_KEY
#     if request.method == 'POST':
#         token = request.POST['stripeToken']
#         print (token)
#         # # Create a charge: this will charge the user's card
#         # try:
#         #     charge = stripe.Charge.create(
#         #         amount=1200,
#         #         currency="usd",
#         #         source=token,
#         #         description="Example Charge"
#         #     )
#         # except strip.error.CardError as e:
#         #     # The card has been declined
#         #     message.info(request, "Your Card Has Been Declined")
#     context = {'publishkey':publishkey}
#     return render(request, 'shop/ch.html')

def search(request):
    return HttpResponse('we are Search')

def tracker(request):
    return HttpResponse('we are Tracker')

def productview(request):
    return HttpResponse('we are Product View')
    