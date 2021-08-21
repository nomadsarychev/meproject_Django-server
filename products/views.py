from django.shortcuts import render
from .models import ProductCategory, Product


# контроллеры


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'products/index.html', context)


def products(request):
    products = Product.objects.all()
    context = {'title': 'Geekshop-Каталог',
               'products': products,
               'categories':ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
