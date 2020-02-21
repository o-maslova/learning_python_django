from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        try:
            user = User.objects.get(username=cleaned_data['username'])
        except Exception:
            raise forms.ValidationError("No such user!")
        if user.password != cleaned_data['password']:
            raise forms.ValidationError("Wrong password!")
        return cleaned_data
