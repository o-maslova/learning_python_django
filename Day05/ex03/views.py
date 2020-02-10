from django.shortcuts import render
from .additional import *


def populate(request):
    page_content = populate_table()
    return render(request, 'populate.html', {'title': "DB insertions",
                                             'data': page_content})


def display(request):
    params = display_table()
    return render(request, 'ex03_display.html', params)
