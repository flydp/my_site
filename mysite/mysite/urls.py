"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from .views import *
from django.conf.urls import url, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^', include('app01.urls',namespace='app01')),
    url(r'^', include('app01.urls')),
    # url(r'^login',login),
    # url(r'^book/([0-9]+)/([a-z]+)/$',book),
    # url(r'^book/(?P<year>[0-9]+)/(?P<title>[a-z]+)/$',book1),
    # path('book/<int:year>/<slug:title>',book1),
    # re_path(r'^book/(\d+)/(\w+)', book),

]
