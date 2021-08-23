from django.db import models
from django.contrib.auth.models import AbstractUser


# Дополнительные поля для пользователя (дополнение в базовый класс)
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
