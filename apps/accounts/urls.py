#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^account/$', views.account, name='account'),
    url(r'^change_account/$', views.change_account, name='change_account'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^change_username/$', views.change_username, name='change_username'),
    url(r'^change_mugshot/$', views.change_mugshot, name='change_mugshot'),
    url(r'^about', views.about, name='about'),
]
