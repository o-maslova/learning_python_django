from django.shortcuts import render
import psycopg2

def init(request):

    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    except psycopg2.OperationalError as err:
        page_content = "<p>" + err + "</p>"
        return render(request, 'init.html', {'title': "Databases", 'data': page_content})

    if connection is not None:
        curr = connection.cursor()
        try:
            curr.execute(
                """ CREATE TABLE IF NOT EXISTS ex00_movies (
                title varchar(64) unique not null,
                episode_nb int primary key,
                opening_crawl text,
                director varchar(32) not null,
                producer varchar(128) not null,
                release_date date not null
                ) """
            )
        except Exception as err:
            page_content = "<p>" + err + "</p>"
            return render(request, 'init.html', {'title': "Databases", 'data': page_content})

        connection.commit()
        connection.close()

    page_content = "<p>OK</p>"
    return render(request, 'init.html', {'title': "Databases", 'data': page_content})
