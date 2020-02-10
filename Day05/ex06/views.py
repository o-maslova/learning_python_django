from django.shortcuts import render
from ex02.additional import *

TABLE = "ex06_movies"


def header():
    return ["", "Title", "Opening crawl", "Director", "Producer", "Release date"]


def alter_table(t_name):
    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        try:
            query = """ ALTER TABLE %s ADD COLUMN IF NOT EXISTS created TIMESTAMP DEFAULT NOW(),
                        ADD COLUMN IF NOT EXISTS updated TIMESTAMP DEFAULT NOW();""" % t_name
            curr.execute(query)
            connection.commit()
            connection.close()
            page_content = "OK"
        except Exception as err:
            page_content = err
    else:
        page_content = connection
    return page_content


def init(request):
    params = {'title': "Initial",
              'data': ""}

    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        data = create_table(TABLE, curr)
        res = data
        if res is "OK":
            res_alter_table = alter_table("ex06_movies")
            params['data'] = "OK"
            if res_alter_table is not "OK":
                params['data'] = res_alter_table
        connection.commit()
        connection.close()
    return render(request, 'init.html', params)


def display(request):
    params = display_table(TABLE)
    params['header'] = header() + ["Created", "Updated"]
    return render(request, 'ex02_display.html', params)


def populate(request):
    params = populate_table(TABLE)
    return render(request, 'populate.html', params)


def update(request):
    return render(request, 'update.html', params)