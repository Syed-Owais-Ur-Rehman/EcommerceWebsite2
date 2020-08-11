from django.contrib import admin

# Register your models here.
# from .models import --model--
from .models import Product
# ,Userid

admin.site.register(Product)
# admin.site.register(Userid)