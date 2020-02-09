from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from .form import PostForm

def out_the_file(data_to_return):
    try:
        fd = open(settings.LOG, 'x')
    except:
        fd = open(settings.LOG, 'r')
        line = fd.readline()
        while line:
            data_to_return += '<p>' + line + '</p>'
            line = fd.readline()
        fd.close()
    return data_to_return


def index(request):
    data_to_return = ""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            fd = open(settings.LOG, 'a')
            data = form.cleaned_data["data_field"]
            date = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            fd.write("Your text: " + data + "\nIt's date: " + date + "\n")
            fd.close()
    form = PostForm()
    data_to_return = out_the_file(data_to_return)
    params = {
        'form': form,
        'data': data_to_return
    }
    return render(request, 'ex02/index.html', params)