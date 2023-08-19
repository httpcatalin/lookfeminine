from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name} ({self.hex_code})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_with_category')
    size_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_with_size_category',default="")
    colors = models.ManyToManyField(Color,null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
    Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image of {self.product.name} - {self.color.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
