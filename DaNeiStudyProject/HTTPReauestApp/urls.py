# _*_ coding: utf-8 _*_
"""
Time:     2023/3/17 17:17
Author:   Sen Zhang
File:     urls.py
Version:  V1.0  2023/3/17 17:17
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
    url(r'01_request/', request_views),
    url(r'02_meta/', request_meta),
    url(r'03_form/', form_views),
    url(r'get_views/', get_views, name='get'),
    url(r'post_views', post_views, name='post_views'),
    url(r'login_form/', login_form,),
    url(r'Remarkforms/', remarkforms, ),
    url(r'loginForms/', loginForms, ),
    url(r'registerForms/', registerForms, ),
    url(r'UsersLoginFormModel/', usersLoginFormModel),
    url(r'UsersRegisterFormModel/', usersRegisterFormModel),
]
urlpatterns += [
    url(r'widget/', widget),
]

