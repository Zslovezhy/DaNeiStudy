# _*_ coding: utf-8 _*_
"""
Time:     2023/3/27 16:54
Author:   Sen Zhang
File:     urls.py
Version:  V1.0  2023/3/27 16:54
Describe: 
Steps:
    1.
    2.
    ...
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'setCookies/', setCookies),
    url(r'getCookies/', getCookies),
    url(r'htmlCookies/', htmlCookies),
]