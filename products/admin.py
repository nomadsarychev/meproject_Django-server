from django.contrib import admin

# Импорт моделей
from products.models import ProductCategory,Product

#Их регистрация в админке.

admin.site.register(Product)
admin.site.register(ProductCategory)