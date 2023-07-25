from django.contrib import admin

# Register your models here.

from .models import Product, Color, Material, Category, Customer, Image, Size

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Customer)
admin.site.register(Image)
admin.site.register(Size)
