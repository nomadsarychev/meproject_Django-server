from django.shortcuts import render, HttpResponseRedirect
from django.urls import  reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from users.models import User
from admin_us.forms import UserRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admin_us/index.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_create(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_us:admin_users'))
#     else:
#         form = UserRegistrationForm()
#     context = {'title': 'GeekShop - Создание пользователя', 'form': form}
#     return render(request, 'admin_us/admin_create.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'admin_us/admin_create.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admin_us:admin_users')


# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {'title': 'GeekShop - Пользователи',
#                'users': User.objects.all()}
#     return render(request, 'admin_us/admin_users.html', context)

class UserListView(ListView):
    model = User
    template_name = 'admin_us/admin_users.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context
    
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_us:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'GeekShop - Редактирвоание пользователя', 'selected_user': selected_user, 'form': form}
#     return render(request, 'admin_us/admin_update.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admin_us/admin_update.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admin_us:admin_users')


# @user_passes_test(lambda u: u.is_staff)
# def admin_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admin_us:admin_users'))

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admin_us/admin_update.html'
    success_url = reverse_lazy('admin_us:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.get_success_url())
