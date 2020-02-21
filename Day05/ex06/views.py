from django.shortcuts import render
from ex02.additional import *
from .models import UpdateForm

TABLE = "ex06_movies"


def header():
    return ["", "Title", "Opening crawl", "Director", "Producer", "Release date"]


def alter_table(t_name):
    connection = create_conn()

    query_trigger = """ CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                        RETURNS TRIGGER AS $$
                        BEGIN
                        NEW.updated = now();
                        NEW.created = OLD.created;
                        RETURN NEW;
                        END;
                        $$ language 'plpgsql';
                        CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                        ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                        update_changetimestamp_column(); """

    if type(connection) is not str:
        curr = connection.cursor()
        try:
            query = """ ALTER TABLE %s ADD COLUMN IF NOT EXISTS created TIMESTAMP DEFAULT NOW(),
                        ADD COLUMN IF NOT EXISTS updated TIMESTAMP DEFAULT NOW();""" % t_name
            curr.execute(query)
            connection.commit()
            curr.execute(query_trigger)
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
        if data is "OK":
            connection.commit()
            res_alter_table = alter_table(TABLE)
            params['data'] = "OK"
            if res_alter_table is not "OK":
                params['data'] = res_alter_table
        connection.commit()
        connection.close()
    else:
        params['data'] = "Something wrong with the server!"
    return render(request, 'init.html', params)


def display(request):
    params = display_table(TABLE)
    params['header'] = header() + ["Created", "Updated"]
    return render(request, 'ex02_display.html', params)


def populate(request):
    params = populate_table(TABLE)
    return render(request, 'populate.html', params)


def update_table(t_name, field, description, title):

    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        query = " UPDATE %s SET %s='%s' WHERE title='%s'; " % (t_name, field, description, title)
        try:
            curr.execute(query)
            data = "OK"
            connection.commit()
            connection.close()
        except Exception:
            data = "No available data!"
    else:
        data = "Something wrong with the server!"
    return data



def update(request):

    params = {'title': "Update data",
              'form': "",
              'data': ""}

    choices = [(el['title'], el['title']) for el in display_table(TABLE)['movie_list']]
    form = UpdateForm(choices=choices)

    if request.method == 'POST':
        form = UpdateForm(request.POST, choices=choices)
        if form.is_valid():
            where = form.cleaned_data['select_movie']
            on_what = form.cleaned_data['movie_description']
            result = update_table(TABLE, 'opening_crawl', on_what, where)
            if result is "OK":
                params['data'] = "You have successfully changed the description of the '{film}' film!".format(film=where)
            else:
                params['data'] = result

    if len(choices) == 0:
        params['data'] = "No available data!"
    else:
        params['form'] = form
    return render(request, 'update.html', params)