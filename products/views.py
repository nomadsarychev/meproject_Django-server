from django.shortcuts import render

# контроллеры

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')