# _*_ coding: utf-8 _*_
"""
Time:     2023/3/7 16:31
Author:   Sen Zhang
File:     urls.py
Version:  V1.0  2023/3/7 16:31
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
    path('admin/', admin.site.urls),
    url(r'login/', login, name='登录'),
    url(r'register/', register, name='注册'),
    url(r'(\d{4})/(\d{2})/', show_args, name='show_args'),
    url(r'02_args/', name_jump,),
    #访问路径为show_reverse的时候，交给reverse_views去处理
    url(r'show_reverse/', reverse_views,)
]