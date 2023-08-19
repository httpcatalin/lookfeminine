from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import stripe
from django.conf import settings
from django.http import JsonResponse

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/index.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    category = Category.objects.all()
    context = {'product': product, 'categories': category}
    return render(request, 'base/product-single.html', context)

def billing(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'products': product}
    return render(request, 'base/formcheckout.html', context)

def checkout(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'products': product}
    return render(request, 'base/checkout.html', context)

def cart(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'products': product}
    return render(request, 'base/cart.html', context)

def shop(request, category_id):
    products = Product.objects.all()
    context = {'products': products, 'category_id': category_id}
    return render(request, 'base/shop.html',context)