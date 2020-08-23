from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    owner = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    # subcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/image", default="")

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address1 = models.CharField(max_length=70)
    address2 = models.CharField(max_length=70)
    customer_email = models.CharField(max_length=70, default="")
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    totalprice = models.FloatField(null=True,default=0)
    phone = models.PositiveIntegerField()
    order_date = models.DateField()


    def __str__(self):
        return self.fname

class Contact(models.Model):
    contact_id = models.AutoField
    contact_name = models.CharField(max_length=20)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=300)
    phone = models.PositiveIntegerField()
    contact_date = models.DateField()


    def __str__(self):
        return self.contact_name