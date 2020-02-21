from django.db import models
from django import forms
from django.forms.widgets import RadioSelect


class Movies(models.Model):

    # Fields
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    # Methods
    def __str__(self):
        return self.title


class RemoveForm(forms.Form):

    def __init__(self, *args, **kwargs):
        ma_choices = kwargs.pop('choices')
        super(RemoveForm, self).__init__(*args, **kwargs)
        self.fields['movies'] = forms.ChoiceField(widget=RadioSelect, choices=ma_choices)
