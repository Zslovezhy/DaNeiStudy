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
from django.template import loader
from django.shortcuts import render


def run_views(request):
    return HttpResponse("第一个Django程序")

def login_php(request):
    """
        1.通过loader加载模板
        2.将模板渲染成字符串
        3.通过HttpResponse响应给客户端
    :param request:
    :return:
    """
    t = loader.get_template("../templates/phpwind_login.html") #1.通过loader加载模板
    html = t.render()#2.将模板渲染成字符串
    return HttpResponse(html)  #3.通过HttpResponse响应给客户端

def login_php1(request):
    """
    使用render直接加载并返回视图
    :param request:
    :return:
    """
    return render(request, "../templates/phpwind_login.html")

def loader_tem(request):
    dic = {
        '变量1': '值1',
        '变量2': '值2',
        '变量3': '值3',
    }
    t = loader.get_template("../templates/send_var.html")
    return HttpResponse(t.render(dic))   #渲染成字符串时需要传递变量字典到模板中

def render_tem(request):
    dic = {
        '1A': 'a',
        '2B': 'b',
        '3C': 'c',
    }
    lst = ['a', 'b', 'c']
    tup = ('A', 'B', 'C')
    vars = {
        'num': 15,
        'str': '模板中的字符串变量',
        'tup': tup,
        'list': lst,
        'dic': dic,
        'fun': fun(1,2),
        'dog': Dog()
    }
    return render(request, '../templates/send_var.html', vars)

def fun(num1, num2):
    return num1 + num2

class Dog(object):
    name = '阿拉斯加'

    def eat(self):
        return '吃狗粮'





