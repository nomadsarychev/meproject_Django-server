from users.form import UserRegistrationForm
from django import forms

from users.models import User


class UserAdminRegistrathon(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'email', 'last_name', 'password1', 'password2')
