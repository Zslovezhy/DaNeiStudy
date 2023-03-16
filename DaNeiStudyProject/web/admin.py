from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']   #指定在列表页中显示的字段
    list_display_links = ['name', 'age']   #指定在列表页中也能链接到详情页的字段们
    list_editable = ['email']    #指定列表页中允许被修改的字段
    search_fields = ['name', 'age', 'email']    #指定允许被搜索的字段们
    list_filter = ['name', 'age', 'email']    #指定在列表页的右侧增加的过滤器允许被筛选的字段们
    #fields = ['email', 'name' ]  #详情页中要显示的字段和显示顺序
    fieldsets = (
        #分组1---name
        (
            '姓名', {
                'fields': ('name',),
            }
        ),
        #分组2---email
        (
            '邮箱',{
                'fields': ('email', 'isActive', 'publisher'),
                'classes': ('collapse', '')
            }
        ),
    )

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publicate_date']
    search_fields = ['title', 'publicate_date']
    date_hierarchy = 'publicate_date'   #时间选择器
    list_display_links = ['title']
    list_editable = ['publicate_date']
    list_filter = ['publicate_date']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city']
    search_fields = ['name', 'address', 'city']
    list_editable = ['address', 'city']
    list_filter = ['country', 'city']
    fieldsets = (
        (
            '基本选项', {
                'fields': ('name', 'address', 'city'),
            }
        ),
        (
            '高级选项', {
                'fields': ('country', 'website'),
                'classes': ('collapse', '')
            }
        )
    )

class AuthorsWifeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_editable = ['age']




# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(AuthorsWife, AuthorsWifeAdmin)

