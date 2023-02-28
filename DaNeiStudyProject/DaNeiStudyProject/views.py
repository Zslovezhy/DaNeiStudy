# _*_ coding: utf-8 _*_
"""
Time:     2023/2/28 15:40
Author:   Sen Zhang
File:     views.py.py
Version:  V1.0  2023/2/28 15:40
Describe:
    编写视图函数，一个函数就是一个独立的处理程序，就是一个独立的视图

"""
from django.http import HttpResponse


def run_views(request):
    return HttpResponse("第一个Django程序")









