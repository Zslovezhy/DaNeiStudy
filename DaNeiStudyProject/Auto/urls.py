# _*_ coding: utf-8 _*_
"""
Time:     2023/2/28 17:07
Author:   Sen Zhang
File:     urls.py.py
Version:  V1.0  2023/2/28 17:07
Describe: 应用Auto中的路由

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index),
]