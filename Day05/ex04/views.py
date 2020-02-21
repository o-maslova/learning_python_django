from django.shortcuts import render
from .models import RemoveForm
from ex02.additional import *


def init(request):
    params = init_connection("ex04_movies")
    return render(request, 'init.html', params)


def display(request):
    params = display_table("ex04_movies")
    params['header'] = ["", "Title", "Opening crawl", "Director", "Producer", "Release date"]
    return render(request, 'ex02_display.html', params)


def populate(request):
    params = populate_table("ex04_movies")
    return render(request, 'populate.html', params)


def delete_entry(t_name, elem):

    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        query = " DELETE FROM %s WHERE title='%s';" % (t_name, elem)
        curr.execute(query)

        connection.commit()
        connection.close()
        return "OK"
    else:
        return connection

def remove(request):
    params = {}
    db = [(el['title'], el['title']) for el in display_table("ex04_movies")['movie_list']]
    form = RemoveForm(choices=db)
    
    if request.method == "GET":
        if len(db) == 0:
            params['data'] = "No available data!"
        params['form'] = form
        params['title'] = "Remove items from table"
    
    if request.method == "POST":
        form = RemoveForm(request.POST, choices=db)
        if form.is_valid():
            data = form.cleaned_data['movies']
            delete_entry("ex04_movies", data)
            db = display_table("ex04_movies")['movie_list']
            form = RemoveForm(choices=[(el['title'], el['title']) for el in db])
            params['form'] = form
        else:
            params['data'] = form.errors

    if len(db) == 0:
        params['data'] = "No available data!"
    return render(request, 'remove.html', params)