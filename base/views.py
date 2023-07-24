from django.shortcuts import render, redirect
from .models import Product, Color, Material, Category

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/index.html', context)
def product(request, pk):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/rochie.html', context)