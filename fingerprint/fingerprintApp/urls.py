from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^appgetstate/$', views.appgetstate),
    url(r'^getstate/$', views.getstate),
    url(r'^updatestate/$', views.updatestate),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
]
