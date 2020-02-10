"""d05 URL Configuration

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
from django.urls import path
from ex00 import views as ex00_views
from ex02 import views as ex02_views
from ex03 import views as ex03_views
from ex04 import views as ex04_views
from ex05 import views as ex05_views
from ex06 import views as ex06_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/init', ex00_views.init, name='ex00_init'),
    path('ex02/init', ex02_views.init, name='ex02_init'),
    path('ex02/populate', ex02_views.populate, name='ex02_populate'),
    path('ex02/display', ex02_views.display, name='ex02_display'),
    path('ex03/display', ex03_views.display, name='ex03_display'),
    path('ex03/populate', ex03_views.populate, name='ex03_populate'),
    path('ex04/init', ex04_views.init, name='ex04_init'),
    path('ex04/display', ex04_views.display, name='ex04_display'),
    path('ex04/populate', ex04_views.populate, name='ex04_populate'),
    path('ex04/remove', ex04_views.remove, name='ex04_remove'),
    path('ex05/display', ex05_views.display, name='ex05_display'),
    path('ex05/populate', ex05_views.populate, name='ex05_populate'),
    path('ex05/remove', ex05_views.remove, name='ex05_remove'),
    path('ex06/init', ex06_views.init, name='ex06_init'),
    path('ex06/display', ex06_views.display, name='ex06_display'),
    path('ex06/populate', ex06_views.populate, name='ex06_populate'),
    path('ex06/update', ex06_views.update, name='ex06_update'),
]
