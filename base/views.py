from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse


def homepage(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/index.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    category = Category.objects.all()
    context = {'product': product, 'categories': category}
    return render(request, 'base/product-single.html', context)


def checkout(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'products': product}
    return render(request, 'base/checkout.html', context)


def shop(request, category_id):
    products = Product.objects.all()
    context = {'products': products, 'category_id': category_id}
    return render(request, 'base/shop.html', context)


def conf(request):
    return render(request, 'base/confirmation.html')


def cart_detail(request):
    cart = request.session.get('cart', {})

    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())

    return render(request, 'base/cart.html', {'cart': cart, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:

        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
