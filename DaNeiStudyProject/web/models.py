from django.db import models

# Create your models here.

class Publisher(models.Model):  # 创建 Publisher 实体类

    # 表示 出版社 的信息,属性如下:
    name = models.CharField(max_length=30, verbose_name='出版社')  #1.name : 出版社的名称(varchar,string)
    address = models.CharField(max_length=50, verbose_name='详细地址')   # 2.address : 出版社的地址
    city = models.CharField(max_length=20, verbose_name='城市')  # 3.city : 出版社所在城市
    country = models.CharField(max_length=20, verbose_name='地区')   # 4.country : 出版社所在国家
    website = models.URLField(verbose_name='网址')     # 5.website : 出版社的网址

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):

    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱')
    isActive = models.BooleanField(default=True, verbose_name='激活')
    publisher = models.ManyToManyField(Publisher, verbose_name='出版社')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name
        ordering = ["-age", "-name"]


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版日期')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name
        ordering = ["publicate_date"]

class AuthorsWife(models.Model):

    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "authorsWife"
        verbose_name = "作者的妻子"
        verbose_name_plural = verbose_name



















