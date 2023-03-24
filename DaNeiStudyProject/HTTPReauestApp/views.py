from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
from django.views.decorators.csrf import csrf_protect


def request_views(request):
    """
        ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__'
, '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_
get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts',
'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_a
jax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
    :param request:
    :return:
    """
    scheme = request.scheme
    body = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES
    meta = request.META
    return render(request, 'request.html', locals())

def request_meta(request):
    if 'HTTP_REFERER' in request.META:
        print('请求的源地址为：' + request.META['HTTP_REFERER'])
    return HttpResponse("Requesr OK!")

def form_views(request):
    return render(request, 'form_views.html')

def get_views(request):
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    return HttpResponse("用户名：" + uname + ",密码：" + upwd)

#@csrf_protect
def post_views(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse("用户名：" + uname + ",密码：" + upwd)

def login_form(request):
    if request.method == 'GET':
        return render(request, 'login_form.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse("用户名：" + uname + ",密码：" + upwd)

def remarkforms(request):
    form = RemarkForm()
    return render(request, 'remarkForm.html', locals())

def loginForms(request):
    if request.method == 'GET':
        forms = LoginForm()
        return render(request, 'loginForm.html', locals())
    else:
        #第一种接收提交的数据
        # uname = request.POST['uname']
        # upwd = request.POST['upwd']
        #第二种接收提交的数据
        forms = LoginForm(request.POST)
        if forms.is_valid():
            c_data = forms.cleaned_data
            uname = c_data['uname']
            upwd = c_data['upwd']
            Ulist = Users.objects.filter(uname=uname, upwd=upwd)
            if Ulist:
                return HttpResponse("用户名：" + uname + ",密码：" + upwd)
            else:
                forms = LoginForm()
                errMsg = "用户名或密码不正确"
                return render(request, 'loginForm.html', locals())

def registerForms(request):
    if request.method == 'GET':
        forms = RegisterForm()
        return render(request, 'RegisterForm.html', locals())
    else:
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            all_data = forms.cleaned_data
            uname = all_data['uname']
            upwd = all_data['upwd']
            uage = all_data['uage']
            uemail = all_data['uemail']
            Ulist = Users.objects.filter(uname=uname, upwd=upwd, uage=uage, uemail=uemail)
            if Ulist:
                warnMsg = "用户已存在"
                forms = RegisterForm()
                return render(request, 'RegisterForm.html', locals())
            else:
                Users.objects.create(uname=uname, upwd=upwd, uage=uage, uemail=uemail)
                succMsg = "注册成功，去登录"
                return HttpResponse("注册成功\n" + "欢迎：\n" + "  用户名：" + uname + "   密码：" + upwd)

def usersLoginFormModel(request):
    if request.method == 'GET':
        forms = UsersLoginFormModel()
        return render(request, 'UsersLoginFormModel.html', locals())

def usersRegisterFormModel(request):
    if request.method == 'GET':
        forms = UsersRegisterFormModel()
        return render(request, 'UsersRegisterFormModel.html', locals())

def widget(request):
    form = WidgetForm()
    return render(request, 'widget.html', locals())
















