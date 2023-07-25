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
    return render(request, 'base/rochie.html', context)


