from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admin_us.forms import UserRegistrationForm


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admin_us/index.html', context)


def admin_create(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_us:admin_users'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Создание пользователя', 'form': form}
    return render(request, 'admin_us/admin_create.html', context)




def admin_users(request):
    context = {'title': 'GeekShop - Пользователи',
               'users': User.objects.all()}
    return render(request, 'admin_us/admin_users.html', context)
