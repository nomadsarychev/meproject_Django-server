from django.urls import path
from admin_us.views import index, admin_users, admin_create

app_name = 'admin_us'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('create/', admin_create, name='admin_create')
]
