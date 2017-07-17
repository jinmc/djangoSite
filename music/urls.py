from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]