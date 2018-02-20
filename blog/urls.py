#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
