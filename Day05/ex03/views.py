from django.shortcuts import render
from .models import Movies

def populate(request):

    page_content = ""

    for entry in film_data():
        movie = Movies(episode_nb=entry['episode_nb'],
                       title=entry['title'],
                       director=entry['director'],
                       producer=entry['producer'],
                       release_date=entry['release_date'])
        if movie:
            movie.save()
            page_content += "<p>'{name}' insertion is OK</p>".format(name=movie.title)
    return render(request, 'populate.html', {'title': "DB insertions",
                                             'data': page_content})



def display(request):
    # page_content = ""

    movies_list = Movies.objects.all()

    return render(request, 'display.html', {'title': "Table content",
                                            'file_name': 'style.css',
                                            'movie_list': movies_list})


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