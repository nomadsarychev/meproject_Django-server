from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.form import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket

# Контролеры
from users.models import User


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    title = f'Подверждение учетной записи {user.username}'

    message = f'Для подтверждение учетной записи{user.username} на портале {settings.DOMAIN_NAME}' \
              f'пройдите по ссылке:\n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'Geekshop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Вы на правильном пути')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'Geekshop - Регитсрация', 'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили профиль!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def verify(reqiest, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expires():
            user.is_active = True
            user.save()
            auth.login(reqiest, user)
            return render(reqiest, 'users/verification.html')
        else:
            print(f'error activation user {user} ')
            return render(reqiest, 'users/verification.html')
    except Exception as err:
        print(f'error activation user {err.args} ')
        return HttpResponseRedirect(reverse('index'))

