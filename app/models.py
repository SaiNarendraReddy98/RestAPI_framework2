from django.db import models

# Create your models here.

class Product_catogry(models.Model):
    product_catogry_id = models.IntegerField(primary_key=True)
    product_catogry_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_catogry_name
    

class Products(models.Model):
    product_catogry_id = models.ForeignKey(Product_catogry,on_delete=models.CASCADE)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_brand = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
    


    