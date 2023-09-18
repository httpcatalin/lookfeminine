from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(size_cat)
admin.site.register(Image)
admin.site.register(Customer)
admin.site.register(Order)


