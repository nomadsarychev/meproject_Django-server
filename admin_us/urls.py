from django.urls import path
from admin_us.views import index, admin_users, admin_create, admin_update, admin_delete

app_name = 'admin_us'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('create/', admin_create, name='admin_create'),
    path('update/<int:id>/', admin_update, name='admin_update'),
    path('delete/<int:id>/', admin_delete, name='admin_delete')
]
