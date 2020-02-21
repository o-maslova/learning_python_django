from django.shortcuts import render
from .additional import *


def init(request):
    params = init_connection()
    return render(request, 'init.html', params)

def display(request):
    params = {
        'title': "Table content",
        'header': ["Character name", "Planet", "Planet climate"],
        'file_name': 'style.css',
        'data': ""
    }

    connection = create_conn()

    if type(connection) != str:
        curr = connection.cursor()
        query = """ SELECT ex08_people.name, ex08_planets.name, ex08_planets.climate
                    FROM ex08_people
                    INNER JOIN ex08_planets ON ex08_people.homeworld=ex08_planets.name
                    WHERE ex08_planets.climate LIKE '%windy%'
                    ORDER BY ex08_people.name DESC """
        curr.execute(query)
        result = curr.fetchall()
        if len(result) != 0:
            params['list'] = result
        else:
            params['data'] = "No available data!"
        connection.close()
    else:
        params['data'] = "Some error!"
    return render(request, 'ex08_display.html', params)


def populate(request):
    params = populate_tables()
    return render(request, 'populate.html', params)