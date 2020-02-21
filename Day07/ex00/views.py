from django.shortcuts import render, redirect
from ex00.models import Article, UserFavouriteArticle
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView, DetailView
from ex00.forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as login_user


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class LoginView(TemplateView):
    form = LoginForm()

    def get_context_data(self, request, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return HttpResponse(render(request, 'login.html', context))

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.form
        return HttpResponse(render(request, 'login.html', context))

    def post(self, request,  *args, **kwargs):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            obj = User.objects.get(username=username)
            user = authenticate(request, username=obj.username, password=obj.password)
            login_user(request, obj)
            return redirect('articles')
        else:
            context['form'] = LoginForm(request.POST)
        return HttpResponse(render(request, 'login.html', context))


class PublicationView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {}
        try:
            articles_list = Article.objects.filter(author=request.user)
        except Exception:
            articles_list = ''
            context['error'] = "You have no articles!"
        context['articles_list'] = articles_list
        return HttpResponse(render(request, 'publications.html', context))


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        logout(request)
        print(request.user)
        return redirect('/')


class FavouritesView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {}
        try:
            user = User.objects.get(username=request.user)
            print(user)
            favourites = UserFavouriteArticle.objects.filter(user=user.pk)
            print(favourites)
        except Exception:
            favourites = ''
            context['error'] = "You have no articles!"
        context['favourites'] = favourites
        return HttpResponse(render(request, 'favourites.html', context))
