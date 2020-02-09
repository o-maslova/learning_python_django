from django.shortcuts import render


def django(request):
    title = "Ex01: Django, framework web engine."
    params = {
        'title': title,
        'content': 'django.html',
        'file_name': 'style1.css'
    }
    return render(request, 'base.html', params)


def display(request):
    title = "Ex01: Process for displaying a static page."
    params = {
        'title': title,
        'content': 'display.html',
        'file_name': 'style1.css'
    }
    return render(request, 'base.html', params)


def templates(request):
    title = "Ex01: Template engine."
    params = {
        'title': title,
        'content': 'templates.html',
        'file_name': 'style2.css'
    }
    return render(request, 'base.html', params)
