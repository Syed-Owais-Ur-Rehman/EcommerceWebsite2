from django.conf import settings
import stripe
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
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
    # print(products)
    #n = len(products)

    # params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products}
    # allprods = [[products, range(1,nslides), nslides],
    #            [products, range(1,nslides), nslides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def dashboard(request):
    if request.user.is_authenticated:
        allprods = []
        catprods = Product.objects.values('owner', 'id')
        cats = {item['owner'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(owner=cat)
            n = len(prod)
            nslides = n//4 + ceil((n/4)-(n//4))
            allprods.append([prod, range(1, nslides), nslides])

        params = {'allprods': allprods}

    else:
        return redirect("/shop/error")

    return render(request, 'shop/dashboard.html', params)


def addform(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request)
            name = request.POST.get('name', '')
            owner = request.POST.get('loggedinuser')
            category = request.POST.get('category', '')
            email = request.POST.get('email', '')
            price = request.POST.get('price', '')
            desc = request.POST.get('desc', '')
            image = request.FILES['image']
            pub_date = request.POST.get('date', '')
            addform = Product(product_name=name, owner=owner, email=email, price=price,
                              desc=desc, image=image, category=category, pub_date=pub_date)
            addform.save()
            return redirect("/shop/dashboard/")
    else:
        return redirect("/shop/error")
    return render(request, 'shop/addform.html')


def login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("/shop/dashboard")
    else:
        if request.method == "POST":
            # Get the post parameters
            loginusername = request.POST['username']
            loginpassword = request.POST['password']

            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                dj_login(request, user)
                context['user'] = request.user
                return redirect("/shop/dashboard")
            else:
                messages.error(request, "Invalid Credentials, Please Try Again")
                return redirect("/shop/login")
    
    return render(request, 'shop/login.html', context)


def logout(request):
    dj_logout(request)
    messages.success(request, "Successfully Logged Out")
    return render(request, 'shop/logout.html')


def signup(request):
    if request.method == "POST":
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

    # check errors

    return render(request, 'shop/signup.html')


def success(request):
    context = {}
    context['user'] = request.user
    messages.success(request, "Your Account Has Been Successfully Created")
    return render(request, 'shop/success.html', context)
check = 0

def cart(request):
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods': allprods}
    return render(request, 'shop/cart.html', params)


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    params = {}
    publishkey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
            token = request.POST.get('stripeToken')
            print(token)
            print('Data:', request.POST)
            order_email = request.POST.get('customeremail')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            add1 = request.POST.get('add1')
            add2 = request.POST.get('add2')
            country = request.POST.get('country')
            city = request.POST.get('city')
            phoneno = request.POST.get('phone')
            orderdate = date.today()
            totalprice = request.POST.get('totalprice')
            customer_amount = request.POST.get('amount')
            orderform = Customer(fname=fname, lname=lname, address1=add1, address2=add2, customer_email=order_email,
                                 country=country, city=city, phone=phoneno, totalprice=totalprice, order_date=orderdate)
            orderform.save()

            try:
                customer = stripe.Customer.create(
                    email=order_email,
                    name=fname + ' ' + lname,
                    balance=customer_amount
                )

                payment = stripe.PaymentIntent.create(
                    customer=customer,
                    amount=customer_amount,
                    # (totalprice*100)
                    currency='usd',
                    payment_method_types=['card'],
                    payment_method='pm_card_visa',
                    source=token,
                    receipt_email=order_email,
                    description='Customer Purchase'
                )
                # charge = stripe.Charge.create(
                #     customer=customer,
                #     amount=customer_amount,
                #     currency="usd",
                #     source=token,
                #     description="Example Charge"
                # )
                return redirect("/shop/transaction/")

            except stripe.error.CardError as e:
                # The card has been declined
                messages.info(request, "Your Card Has Been Declined")

    
    # return redirect("/shop/error")
    context = {'publishkey': publishkey}
    return render(request, 'shop/checkout.html', context)


def error(request):
    return render(request, 'shop/error.html')

def transaction(request):
    return render(request, 'shop/transaction.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/productview.html', {'product': product[0]})
