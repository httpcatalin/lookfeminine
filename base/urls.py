from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse
from django import forms
import time


def homepage(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())
    context = {'products': products,  'total_price': total_price, "cart": cart}
    return render(request, 'base/index.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    products = Product.objects.all()
    category = Category.objects.all()
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())
    cart_items = list(cart.values())
    context = {'products': products, 'cart': cart, 'product': product,
               'categories': category, 'product_id1': pk, 'total_price': total_price, 'cart_items': cart_items}
    
    return render(request, 'base/product-single.html', context)


def shop(request, category_id):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())
    context = {'products': products, 'category_id': category_id ,'total_price': total_price, "cart": cart}
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
    color_image_mapping = {}
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())
    colors = product.colors.values()
    images = product.image.values()

    for i, color_info in enumerate(colors):
        color_name = color_info['name']

        if i < len(images):
            image_info = images[i]
            image_url = image_info['image']
        else:
            image_url = None

        color_image_mapping[color_name] = image_url

    cart = request.session.get('cart', {})
    selected_color = request.POST.get('selected_color')
    selected_size = request.POST.get('selected_size')

    selected_image_url = color_image_mapping.get(selected_color)

    cart_item_id = f"{product_id}-{int(time.time())}"

    cart[cart_item_id] = {
        'name': product.name,
        'price': int(product.price),
        'quantity': 1,
        'image': selected_image_url,
        'size': selected_size,
        'color': selected_color,
    }
    request.session['cart'] = cart

    action = request.POST.get('action')
    if action == 'Adaugă în coș':
        return redirect('product', product_id)
    elif action == 'Cumpără':
        return redirect('checkout')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart2(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return render(request, 'base/checkout.html', {'total_price': total_price})


def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('shop', 'all')
    total_price = sum(item['price'] for item in cart.values())
    if request.method == 'POST':
        first_name = request.POST['first_name']
        address = request.POST['address']
        phone_number = request.POST['number']
        city = request.POST['city']
        total_price = sum(item['price'] for item in cart.values())
        customer = Customer.objects.create(
            first_name=first_name,
            address=address,
            phone_number=phone_number,
            city=city
        )
        order = Order.objects.create(
            customer=customer,
            address=address,
            phone_number=phone_number,
            city=city,
            products=str(cart),
            total_price=total_price
        )
        request.session['cart'] = {}

        return redirect('confirmation')

    return render(request, 'base/checkout.html', {'cart': cart, 'total_price': total_price})


urlpatterns = [
    path('', homepage, name='home'),
    path('product/<int:pk>/', product, name='product'),
    path('checkout', checkout_view, name='checkout'),
    path('products/<str:category_id>/', shop, name='shop'),
    path('confirmation', conf, name='confirmation'),
    path('cart', cart_detail, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_id>/',
         remove_from_cart, name='remove_from_cart'),
    path('remove-from-cart2/<str:product_id>/',
         remove_from_cart2, name='remove_from_cart2'),
    path('checkout_buy/<int:product_id>/', checkout_view, name='checkout_buy')

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
