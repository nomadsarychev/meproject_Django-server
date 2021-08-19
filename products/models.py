from django.db import models


# id назначается автоматически.Исскуственно можно сделать primary_key= true.uuid
# Модели=таблицы базы данных(написанных в виде классов в python)

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)  # varchar, длина 64, повторяться не могут.
    description = models.TextField(blank=True,
                                   null=True)  # text, параметры говорят что поле может быть не заполнено.


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images',
                              blank=True)  # как и charfield хронит строку (ссылка где находится файл с картинкой upload_to='products_images')
    description = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                default=0)  # числа, 1 занчение сколько цифр до запятой,2 после запятой ,3 по умолчанию 0
    quantity = models.PositiveIntegerField(default=0)  # только положительные зачения
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # внешний ключ, удаление каскадом.

#   миграция - конвертация кода python в sql код.
#   python manage.py makemigrations
#   python manage.py migrate
