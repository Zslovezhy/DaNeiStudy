from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from django.db.models import F, Q

# Create your views here.
def add_views(request):
    #ret = Author.objects.create(name='老舍', age=60, email='laoshe@qq.com')
    #ret1 = Author(name='冰心', age=18, email='bingxin@qq.com')
    #ret1.save()
    dic1 = {
        'name': '施耐庵',
        'age': 55,
        'email': 'SNA@qq.com',
        'isActive': True,
    }
    ret2 = Author(**dic1)
    ret2.save()
    return HttpResponse(ret2)

def add_book_views(request):
    ret = Book.objects.creat(title='《骆驼祥子》', publicate_date='1998-03-15')
    ret1 = Book(title='《简爱》', publicate_date='1998-09-15')
    ret1.save()
    dic = {
        'title': '《西游记》',
        'publicate_date': '2023-03-13',
    }
    ret2 = Book(**dic)
    ret2.save()
    return HttpResponse("Add Book OK")

def add_publisher_views(request):
    ret = Publisher.objects.creat(name='北京出版社', address='北京故宫', city='北京', country='北京', website='www.bjcbs.com')
    ret1 = Publisher(name='上海出版社', address='上海市浦东新区', city='上海', country='上海', website='www.shcbs.com')
    ret1.save()
    dic = {
        'name': '陕西出版社',
        'address': '陕西省西安市',
        'city': '陕西',
        'country': '西安',
        'website': 'www.sxcbs.com',
    }
    ret2 = Publisher(**dic)
    ret2.save()
    return HttpResponse("Add publisher OK")

def query_athor(request):
    athors = Author.objects.all()
    #name_age = Author.objects.values('name', 'age')
    #name = Author.objects.values_list()
    #age_order = Author.objects.order_by('age')
    age_18 = Author.objects.exclude(age=18)
    return HttpResponse(age_18)

def query_athor_html(request):
    authors = Author.objects.filter(isActive=True).order_by("-age")
    return render(request, 'Athor_query.html', locals())

def query_athor_getsigle(request):
    name_bingxin = Author.objects.get(name='海伦')
    return HttpResponse(name_bingxin)

def query_athor_filter(request):
    name_laoshe = Author.objects.filter(name='老舍')
    name_bingxin = Author.objects.filter(name__contains='冰').count()
    return HttpResponse(name_bingxin)

def get_author_info(request, id):
    author_info = Author.objects.get(id=id)
    return render(request, 'Athor_info.html', locals())

def update_author(request):
    old_author = Author.objects.get(id=1)
    old_author.name = '舒庆春'
    old_author.save()
    return HttpResponse("Update OK")

def update_author_group(request):
    old_author = Author.objects.filter(age=60).update(isActive=0)
    return HttpResponse("Update group OK")

def del_author(request, id):
    au = Author.objects.get(id=id)
    au.delete()
    return HttpResponse("Delete OK")

def del_author_group(request):
    au = Author.objects.filter(age__gte=61)
    au.delete()
    return HttpResponse("Delete Group OK")

def del_author_changeIsActive(request, id):
    au = Author.objects.get(id=id)
    au.isActive = False
    au.save()
    url = reverse('all_authors_html')
    #return query_athor_html(request)    #使用转发
    #return HttpResponseRedirect('/web/query_athor_html/')   #使用重定向
    return redirect(url)    #使用name反向解析

def update_age(request):
    #Author.objects.all().update(age=F('age')+10)
    Author.objects.filter(Q(age__lt=40)|Q(age__gt=75)).update(age=F('age')+5)
    return HttpResponse("更新年龄成功")























