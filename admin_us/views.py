from django.shortcuts import render

from users.models import User


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admin_us/index.html', context)


def admin_create(request):
    context = {'title': 'GeekShop - Admin - create'}
    return render(request, 'admin_us/create_user.html', context)


def admin_users(request):
    context = {'title': 'GeekShop - Admin - create',
               'users': User.objects.all()}
    return render(request, 'admin_us/admin_users.html', context)
