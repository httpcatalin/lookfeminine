from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime



class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name} ({self.hex_code})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class size_cat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.image.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size, null=False)
    size_category = models.ForeignKey(
        size_cat, on_delete=models.CASCADE, default="")
    colors = models.ManyToManyField(Color, null=False)
    image = models.ManyToManyField(Image, null=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bestseller = models.BooleanField(default=False)
    

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
    def __str__(self):
        return f"{self.name}"



class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    products = models.TextField()  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order by {self.customer.first_name}"




