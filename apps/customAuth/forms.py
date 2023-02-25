from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
