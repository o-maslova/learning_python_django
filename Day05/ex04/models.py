from django import forms
from django.forms.widgets import RadioSelect


class RemoveForm(forms.Form):

    def __init__(self, *args, **kwargs):
        ma_choices = kwargs.pop('choices')
        super(RemoveForm, self).__init__(*args, **kwargs)
        self.fields['movies'] = forms.ChoiceField(widget=RadioSelect, choices=ma_choices)
