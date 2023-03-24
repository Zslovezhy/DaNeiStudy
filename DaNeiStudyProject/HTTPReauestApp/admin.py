from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register()

class UsersAdmin(admin.ModelAdmin):
    list_display = ['uname', 'uage', 'uemail']   #指定在列表页中显示的字段
    list_display_links = ['uname']   #指定在列表页中也能链接到详情页的字段们
    list_editable = ['uage', 'uemail']    #指定列表页中允许被修改的字段
    search_fields = ['name', 'age', 'uemail']    #指定允许被搜索的字段们

admin.site.register(Users, UsersAdmin)