import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def setCookies(request):
    uname = '张森'
    uname = json.dumps(uname)
    resp = HttpResponse("Set Cookie OK")
    resp.set_cookie('uname', uname, 60*60*24)
    return resp

def getCookies(request):
    uname = request.COOKIES['uname']
    uname = json.loads(uname)
    return HttpResponse(uname)

def htmlCookies(request):
    return render(request, 'htmlCookies.html', locals())

