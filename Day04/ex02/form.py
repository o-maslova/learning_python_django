from django import forms

# from .models import Post

class PostForm(forms.Form):
    data_field = forms.CharField()
