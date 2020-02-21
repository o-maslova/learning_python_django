from django.shortcuts import render
from .models import People, Planets


def display(request):
    params = {
        'title': "Table content",
        'header': ["Character name", "Planet", "Planet climate"],
        'file_name': 'style.css',
        'data': "",
        'list': []
    }

    try:
        res = People.objects.filter(homeworld__pk__in=
                                [elem.pk for elem in Planets.objects.all().filter(
                                    climate__contains='windy')]).order_by('name')
    except Exception:
        params['data'] = "No data available, please use the following command line before use:<br>" \
                         "<h4>python manage.py loaddata ex09/ex09_initial_data.json</h4>"
        return render(request, 'ex09_display.html', params)
    if res.count() != 0:
        for every in res:
            params['list'].append({
                'name': every.name,
                'homeworld': every.homeworld,
                'climate': Planets.objects.get(name=every.homeworld).climate
            })
    else:
        params['data'] = "<p>No data available!</p>"
    return render(request, 'ex09_display.html', params)
