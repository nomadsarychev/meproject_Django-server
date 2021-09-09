from django.urls import path
from admin_us.views import index, UserListView, UserCreateView, UserUpdateView, admin_delete

app_name = 'admin_us'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('create/', UserCreateView.as_view(), name='admin_create'),
    path('update/<int:pk>/',UserUpdateView.as_view(), name='admin_update'),
    path('delete/<int:id>/', admin_delete, name='admin_delete')
]
