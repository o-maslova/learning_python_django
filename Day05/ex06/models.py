from django.db import models
from django import forms

class UpdateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        ma_choices = kwargs.pop('choices')
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['select_movie'] = forms.ChoiceField(choices=ma_choices)
        self.fields['movie_description'] = forms.TextInput()
