from django.shortcuts import render
from .models import Product    #, Contact
from math import ceil


# For Product objects to show use the following code
# ctrl+shift+p > Preferences: Configure Language Specific Settings > Python
# "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django",
#     ]


# Create your views here.
from django.http import HttpResponse

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
        addform = Product(product_name=name, email=email, price=price, desc=desc, image=image, pub_date=pub_date)
        addform.save()
    return render(request, 'shop/addform.html')

def login(request):
    return render(request, 'shop/login.html')

def signup(request):
    return render(request, 'shop/signup.html')  

def checkout(request):
    return render(request, 'shop/checkout.html')

def search(request):
    return HttpResponse('we are Search')

def tracker(request):
    return HttpResponse('we are Tracker')

def productview(request):
    return HttpResponse('we are Product View')