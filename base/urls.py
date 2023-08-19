from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product, name='product'),
    path('billing/<int:pk>/', views.billing, name='billing'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('cart/<int:pk>/', views.cart, name = 'cart'),
    path('products/<str:category_id>/',views.shop, name = 'shop'),
]

