from django.contrib import admin

# Импорт моделей
from products.models import ProductCategory, Product

# Их регистрация в админке.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('name',)
    search_fields = ('name',)
