# _*_ coding: utf-8 _*_
"""
Time:     2023/3/8 14:50
Author:   Sen Zhang
File:     urls.py
Version:  V1.0  2023/3/8 14:50
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
    url(r'01_add/', add_views),
    url(r'add_book/', add_book_views),
    url(r'add_publisher/', add_publisher_views),
    url(r'query_athor/', query_athor),
    url(r'query_athor_html/', query_athor_html, name='all_authors_html'),
    url(r'query_athor_getsingle/', query_athor_getsigle),
    url(r'query_athor_filter/', query_athor_filter),
    url(r'athor_info/(\d+)/', get_author_info, name='author_info'),
    url(r'update_author/', update_author, name='update_author'),
    url(r'update_author_group/', update_author_group, name='update_author_group'),
    url(r'del_author/(\d+)/', del_author, name='del_author'),
    url(r'del_author_group/', del_author_group, name='del_author_group'),
    url(r'del_author_changeIsActive/(\d+)/', del_author_changeIsActive, name='changeIsActive'),
    url(r'update_age/', update_age, name='update_age'),
]
urlpatterns += [
    url(r'findAuthorByWife/', findAuthorByWife, name='findAuthorByWife'),
    url(r'findWifeByAuthor/', findWifeByAuthor, name='findWifeByAuthor'),
    url(r'findPublisherByBook/', findPublisherByBook, name='findPublisherByBook'),
    url(r'findBookByPublisher/', findBookByPublisher, name='findBookByPublisher'),
    url(r'findAuthorByBook/', findAuthorByBook, name='findAuthorByBook'),
    url(r'findBookByAuthor/', findBookByAuthor, name='findBookByAuthor'),
    url(r'findPublisherByAuthor/', findPublisherByAuthor, name='findPublisherByAuthor'),
    url(r'findAuthorByPublisher/', findAuthorByPublisher, name='findAuthorByPublisher'),
]