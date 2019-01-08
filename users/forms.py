from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    steamId = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'steamId', 'password1', 'password2']
