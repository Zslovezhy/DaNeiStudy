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
]
urlpatterns += [
    url(r'^phpwind/', login_php),
    url(r'^phpwind1/', login_php1),
    url(r'^loader/', loader_tem),
    url(r'^render/', render_tem),
]
