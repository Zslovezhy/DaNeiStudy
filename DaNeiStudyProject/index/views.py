from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

#/show/四位数字/两位数字
def show_args(request, num1, num2):
    return HttpResponse('参数1：' + num1 + '参数2：' + num2)

def name_jump(request):
    return render(request, '02_args_name.html')

#show_reverse路径对应的视图
def reverse_views(request):
    #将‘注册’别名解析成对应的url（无参）
    #url = reverse('注册')
    #将‘show_args’别名解析成对应的url（带参）
    url = reverse('show_args', args=('2023', '38',))
    return HttpResponse('解析地址为：' + url)
