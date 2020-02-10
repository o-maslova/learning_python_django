from django.shortcuts import render
from ex03.additional import *
from .models import RemoveForm

def populate(request):
    page_content = populate_table()
    return render(request, 'populate.html', {'title': "DB insertions",
                                             'data': page_content})


def display(request):
    params = display_table()
    return render(request, 'ex03_display.html', params)


def remove(request):

    params = {'title': "Remove items from table"}
    lst_of_titles = [(elem.title, elem.title) for elem in Movies.objects.all()]
    form = RemoveForm(choices=lst_of_titles)

    if request.method == "GET":
        if len(lst_of_titles) == 0:
            params['data'] = "No available data!"
        else:
            params['form'] = form

    if request.method == "POST":
        form = RemoveForm(request.POST, choices=lst_of_titles)
        if form.is_valid():
            data = form.cleaned_data['movies']
            object = Movies.objects.get(title=data)
            if object:
                object.delete()
                form = RemoveForm(choices=[(elem.title, elem.title) for elem in Movies.objects.all()])
                params['form'] = form
        else:
            params['data'] = form.errors

    if len(lst_of_titles) == 0:
        params['data'] = "No available data!"
    return render(request, 'remove.html', params)