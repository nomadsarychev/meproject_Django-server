from django.shortcuts import render
from products.models import ProductCategory, Product


# контроллеры


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Geekshop-Каталог',
               'categories': ProductCategory.objects.all(),
               }
    products = Product.objects.filter(
        category_id=category_id) if category_id else Product.objects.all()  # можно сразу записать в словарь
    context['products'] = products
    return render(request, 'products/products.html', context)
