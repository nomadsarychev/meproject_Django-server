from django.contrib import admin

# Register your models here.
from orderapp.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
