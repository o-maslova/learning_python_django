from django.db import IntegrityError
from ex03.models import Movies
from ex05.models import Movies
from ex07.models import Movies


def populate_table():
    page_content = ""

    for entry in film_data():
        try:
            try:
                movie = Movies.objects.create(episode_nb=entry['episode_nb'],
                                              title=entry['title'],
                                              director=entry['director'],
                                              producer=entry['producer'],
                                              release_date=entry['release_date'])
                movie.save()
                page_content += "<p>'{name}' insertion is OK</p>".format(name=movie.title)
            except Exception:
                page_content = "No available data!"
        except IntegrityError:
            page_content += "<br>'{film}' film is already exist!".format(film=entry['title'])
            break
    return page_content


def display_table():
    params = {
        'title': "Table content",
        'file_name': 'style.css',
        'header': ["", "Title", "Opening crawl", "Director", "Producer", "Release date"],
    }

    try:
        movies_list = Movies.objects.all()
        if movies_list.count() == 0:
            params.update({'data': "No available data!"})
        else:
            params.update({'movie_list': movies_list})
    except Exception:
        params.update({'data': "No available data!"})
    return params


def film_data():
    return [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kutz, Rick McCallum',
            'release_date': '1980-05-17'
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25'
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11'
        }
    ]