from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
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

# class Userid(models.Model):
#     msg_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=70, default="")
#     phone = models.CharField(max_length=70, default="")
#     desc = models.CharField(max_length=500, default="")


#     def __str__(self):
#         return self.name