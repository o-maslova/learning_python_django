from django import forms
from django.forms import ModelForm
from .models import Tip
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterForm(forms.Form):
    user_name = forms.CharField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)


class LoginForm(forms.Form):

    user_name = forms.CharField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']


class CreateTip(forms.Form):
    content = forms.CharField(required=True)

    class Meta:
        model = Tip
        fields = ['content']