# _*_ coding: utf-8 _*_
"""
Time:     2023/3/20 16:52
Author:   Sen Zhang
File:     forms.py
Version:  V1.0  2023/3/20 16:52
"""
from django import forms
from .models import *

TOPIC_CHOICE = (
    ('1', '好评'),
    ('2', '中评'),
    ('3', '差评'),
)
#评论内容的表单控件
class RemarkForm(forms.Form):
    subject = forms.CharField(label='Title')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)  #widget=forms.Textarea:小部件，多行文本框
    topci = forms.ChoiceField(label='Topic', choices=TOPIC_CHOICE)
    isSaved = forms.BooleanField(label='IsSaved')

class LoginForm(forms.Form):
    uname = forms.CharField(label='用户名')
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名')
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    uage = forms.IntegerField(label='年龄')
    uemail = forms.EmailField(label='邮箱')

#关联到Users实体类
class UsersLoginFormModel(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['uname', 'upwd']
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码',
        }
class UsersRegisterFormModel(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['uname', 'upwd', 'uage', 'uemail']
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码',
            'uage': "年龄",
            'uemail': '邮箱'
        }

class WidgetForm(forms.Form):
    uname = forms.CharField(
        label='用户名',
        widget=forms.TextInput(
            attrs={
                'name': 'user_name',
                'placeholder': '请输入用户名',
                'class': 'form-control',
            }
        ),
    )
    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput(
            attrs={
                'name':'user_pwd',
                'placeholder': '请输入密码',
                'class': 'form-control',
            }
        )
    )




