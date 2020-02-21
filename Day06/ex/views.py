from django.shortcuts import render, redirect
import random
from d06.settings import USER_NAMES
from .forms import LoginForm, RegisterForm, CreateTip
from .models import Tip, Like, Dislike
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, authenticate


def random_name():
    return random.choice(USER_NAMES)


def get_name(request):

    if 'username' not in request.session:
        request.session['username'] = random_name()
        request.session.set_expiry(42)
        username = request.session['username']
    if request.session.get('username', False) is False:
        request.session['username'] = random_name()
        username = request.session['username']
    else:
        username = request.session['username']
    return username


def index(request):

    content = {
        'username': ""
    }

    content['tips'] = Tip.objects.all()

    content['tips'] = content['tips'].order_by('content')
    content['username'] = get_name(request)
    print(content['username'])
    if request.user.is_authenticated:
        response = render(request, 'display_tips.html', content)
    else:
        response = render(request, 'index.html', content)
    return response


def login(request):

    content = {
        'username': "",
        'form': "",
        'error': ""
    }

    if 'logged_in' in request.session:
        return redirect('/')

    if request.method == "GET":
        request.session.flush()
        form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            try:
                object = User.objects.get(username=username)
                if object.password == password:
                    request.session['username'] = username
                    content['username'] = username
                    request.session['logged_in'] = True
                    login_user(request, object)
                    return redirect('/')
                else:
                    content['error'] = "Wrong password!"
            except Exception:
                form = LoginForm(request.POST)
                content['error'] = "No such user! Please, register at first."

    content['form'] = form
    return render(request, 'login.html', content)


def register(request):

    content = {
        'username': "",
        'form': "",
        'error': ""
    }

    if 'logged_in' in request.session:
        return redirect('/')

    if request.method == "GET":
        request.session.flush()
        form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password == password_confirm:
                try:
                    new_user = User.objects.create(username=username, password=password)
                    new_user.save()
                    request.session['username'] = username
                    content['username'] = username
                    request.session['logged_in'] = True
                    login_user(request, new_user)
                    return redirect('/')
                except IntegrityError:
                    form = RegisterForm(request.POST)
                    content['error'] = "Username already exist!"
            else:
                content['error'] = "Passwords not match!"

    content['form'] = form
    return render(request, 'register.html', content)


def logout(request):

    request.session.flush()
    return redirect('/')


def create_tip(request):
    content = {
        'username': "",
        'form': "",
        'error': ""
    }

    form = CreateTip()

    if request.method == "POST":
        form = CreateTip(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            object = User.objects.get(username=request.session['username'])
            try:
                tip = Tip(content=content, author=object)
                tip.save()
                return redirect('/')
            except Exception:
                content['error'] = "Something wrong!"
                return render(request, 'create_tip.html', content)

    content['form'] = form
    return render(request, 'create_tip.html', content)


def upvote(request, pk):

    obj = Tip.objects.get(pk=pk)
    try:
        like = Like.objects.get(author=request.user, tip=obj)
        like.delete()
        obj.up_vote -= 1
        obj.save()
    except Exception:
        like = Like.objects.create(author=request.user, tip=obj)
        like.save()
        obj.up_vote += 1
        obj.save()
    return redirect('/')


def downvote(request, pk):

    obj = Tip.objects.get(pk=pk)
    try:
        dislike = Dislike.objects.get(author=request.user, tip=obj)
        dislike.delete()
        obj.down_vote -= 1
        obj.save()
    except Exception:
        try:
            like = Like.objects.get(author=request.user, tip=obj)
            like.delete()
            dislike = Dislike.objects.create(tip=obj, author=request.user)
            dislike.save()
            obj.down_vote += 1
            obj.up_vote -= 1
            obj.save()
        except:
            pass
    return redirect('/')
