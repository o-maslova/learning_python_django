"""d04 URL Configuration

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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from ex00 import views as ex00_views
from ex01 import views as ex01_views
from ex02 import views as ex02_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', ex00_views.index, name='index'),
    path('ex01/django', ex01_views.django, name='django'),
    path('ex01/display', ex01_views.display, name='display'),
    path('ex01/templates', ex01_views.templates, name='templates'),
    path('ex02/', ex02_views.index, name='index'),
]

