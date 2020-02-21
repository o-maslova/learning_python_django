from django.shortcuts import render
from ex03.additional import *
from ex06.models import UpdateForm


def populate(request):
    page_content = populate_table()
    return render(request, 'populate.html', {'title': "DB insertions",
                                             'data': page_content})


def display(request):
    params = display_table()
    params['header'] += ["Created", "Updated"]
    return render(request, 'ex07_display.html', params)


def update(request):

    params = {'title': "Update data",
              'form': "",
              'data': ""}

    lst_of_titles = [(elem.title, elem.title) for elem in Movies.objects.all()]
    form = UpdateForm(choices=lst_of_titles)

    params['form'] = form

    if Movies.objects.count() != 0:
        if request.method == "POST":
            form = UpdateForm(request.POST, choices=lst_of_titles)
            if form.is_valid():
                where = form.cleaned_data['select_movie']
                on_what = form.cleaned_data['movie_description']
                object = Movies.objects.get(title=where)
                if object:
                    params['data'] = "You have successfully changed the description of the '{film}' film!".format(film=where)
                    object.opening_crawl = on_what
                    object.save()
    else:
        params['data'] = "No available data!"
    return render(request, 'update.html', params)