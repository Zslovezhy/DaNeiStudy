from django.db import models

# Create your models here.
class Users(models.Model):
    uname = models.CharField(max_length=50, verbose_name='用户名')
    upwd = models.CharField(max_length=50, verbose_name='密码')
    uage = models.IntegerField(max_length=20, verbose_name='年龄')
    uemail = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = "Users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

