from django.shortcuts import render
from .additional import create_conn, insertion, create_page_content, film_data

def init(request):

    connection = create_conn()

    if type(connection)is not str:
        curr = connection.cursor()
        try:
            curr.execute(
                """ CREATE TABLE IF NOT EXISTS ex02_movies (
                title varchar(64) unique not null,
                episode_nb int primary key,
                opening_crawl text,
                director varchar(32) not null,
                producer varchar(128) not null,
                release_date date not null
                ) """
            )
        except Exception as err:
            return render(request, 'init.html', {'title': "Initial",
                                                 'data': err})

        connection.commit()
        connection.close()

    return render(request, 'init.html', {'title': "Initial",
                                         'data': "OK"})


def populate(request):

    page_content = ""

    connection = create_conn()

    if type(connection)is not str:
        curr = connection.cursor()
        for elem in film_data():
            res = insertion(curr, elem)
            if res is not "OK":
                return render(request, 'populate.html', {'title': "DB insertions",
                                                         'data': create_page_content(res)})
            else:
                page_content += create_page_content("'{elem}' insertion is {res}".format(elem=elem['title'],
                                                                                        res=res))

        connection.commit()
        connection.close()

    return render(request, 'populate.html', {'title': "DB insertions",
                                             'data': page_content})


def make_beautiful_output(data):
    lst = []
    for elem in data:
        lst.append({
            'title': elem[0],
            'episode_nb': elem[1],
            'opening_crawl': elem[2],
            'director': elem[3],
            'producer': elem[4],
            'release_date': elem[5]
        })
    return lst

def display(request):

    page_content = []

    connection = create_conn()

    if type(connection)is not str:
        curr = connection.cursor()
        try:
            curr.execute(" SELECT * FROM ex02_movies ")
        except Exception:
            return render(request, 'display.html', {'title': "Table content",
                                                    'data': "No data available"})
        response = curr.fetchall()
        page_content = make_beautiful_output(response)
        connection.close()
    return render(request, 'display.html', {'title': "Table content",
                                            'file_name': 'style.css',
                                            'movie_list': page_content})