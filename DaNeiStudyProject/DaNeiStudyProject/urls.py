"""DaNeiStudyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^Auto/', include('Auto.urls'), name="交给Auto应用去处理，转交给Auto的urls"),
    url(r'^index/', include('index.urls'), name="交给index应用去处理，转交给index的urls"),
    url(r'^web/', include('web.urls'), name="交给web应用去处理，转交给web的urls"),
    url(r'^HTTPReauestApp/', include('HTTPReauestApp.urls'), name="交给HTTPReauestApp应用去处理，转交给HTTPReauestApp的urls"),
    url(r'^AjaxStudy/', include('AjaxStudy.urls'), name="交给Ajax_Study应用去处理，转交给Ajax_Study的urls"),
]
urlpatterns += [
    url(r'^phpwind/', login_php),
    url(r'^phpwind1/', login_php1),
    url(r'^loader/', loader_tem),
    url(r'^render/', render_tem),
    url(r'01_static/', static_views),
]
