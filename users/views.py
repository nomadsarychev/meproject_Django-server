from django.shortcuts import render


# Контролеры

def login(request):
    context = {'title': 'Geekshop - Авторизация'}
    return render(request, 'users/login.html')


def registration(request):
    context = {'title': 'Geekshop - Регитсрация'}
    return render(request, 'users/registration.html')
