"""d07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ex00.views import ArticleListView, PublicationView, LoginView, ArticleDetailView, LogoutView, FavouritesView
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/articles"), name="home"),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('publications/', PublicationView.as_view(), name="publications"),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('favourites/', FavouritesView.as_view(), name="favourites"),
]
