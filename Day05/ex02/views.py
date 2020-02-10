from django.shortcuts import render
from .additional import init_connection, display_table, populate_table

def init(request):
    params = init_connection("ex02_movies")
    return render(request, 'init.html', params)


def display(request):
    params = display_table("ex02_movies")
    params['header'] = ["", "Title", "Opening crawl", "Director", "Producer", "Release date"]
    return render(request, 'ex02_display.html', params)


def populate(request):
    params = populate_table("ex02_movies")
    return render(request, 'populate.html', params)