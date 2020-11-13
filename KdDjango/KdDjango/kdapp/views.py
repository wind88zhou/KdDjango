from django.shortcuts import render,redirect #导入简单的重定向函数
from django.http import HttpResponse, JsonResponse,FileResponse,HttpResponseRedirect
from kdapp  import models
from kdapp.models import BookInfo
from kdapp.My_forms import EmpForm
from django.core.exceptions import ValidationError
from datetime import date,datetime,timedelta
# Create your views here

def showAppMsg(request):
    return JsonResponse({"errcode": 402545,"description": "request method is wrong!"})

def addemp(request):
   #  return JsonResponse({"errcode": 8885,"description": "reqaaaauest method is wrong!"})
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "addemp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "addemp.html", {"form": form, "clear_errors": clear_errors})

def index(request):
    # 显示图书信息
    books = BookInfo.objects.all()
    return render(request,"index.html",{'books':books})

def create(request):
    #  新增一本图书   sdsad
    b = BookInfo()
    b.btitle = "lxhdj"
    b.bpub_data = date(1990,1,1)
    b.save()

    # return HttpResponseRedirect('index') 简写如下一句
    return redirect('index')

def delete(request,bid):
    # 删掉点击的图书
    book = BookInfo.objects.get(id = bid)
    book.delete()
    # return HttpResponseRedirect('index') 简写如下一句
    return redirect('index')

def login(request):
    # 获取cookie  username
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''

    return render(request,"login.html",{'username':username})


def longin_check(request):
    '''登录校验视图'''
    # 1、获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)
    # 2、进行登录校验
    if username == 'smart' and password =='123':
        # 用户名、密码正确
        response = redirect('index')
        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置cookie username 过期时间为60s
            response.set_cookie('username',username,max_age=60)
        return response
    else:
        # 用户名、密码错误
        return redirect('login')
    # 3、返回应答

# 缺失js文件，未完！
def login_ajax(request):

    return render(request,'login_ajax.html')

# /set_cookie
def set_cookie(request):
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num，值为1
    # 设置cookie 60s后过期
    response.set_cookie('num',1,max_age=60)
    # 设置cookie 2周之后过去
    # response.set_cookie('num',1,expires=datetime.now()+timedelta(days=14))
    # 返回response
    return response

# /get_cookie
def get_cookie(request):
    # 去除cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)

# /set_session
def set_session(request):
    # 设置session
    request.session['username'] = 'smart'
    request.session['age'] = 18
    request.session.set_expiry(10) # 设置10秒过期
    return HttpResponse('设置session@!!')

# /get_session
def get_session(request):
    # 获取session
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

def clear_session(request):
    request.session.clear()
    return HttpResponse('清除成功!')

# 传给模板的变量
def temp_var(request):
    my_dict = {'title':'字典键值'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=1)

    context = {'my_dict':my_dict,"my_list":my_list,'book':book}

    return render(request,'temp_var.html',context)

# 模板标签的使用
def temp_tags(request):
    books = BookInfo.objects.all()
    return render(request,'temp_tags.html',{'books':books})

# 模板继承的使用
def temp_inherit(request):
    return render(request, 'child.html')

# html转义
def html_escape(request):
    return render(request,'html_escape.html',{'content':'<h1>hello</h1>'})

# 静态文件显示
def static_test(request):
    # 获取浏览器的IP地址
    user_ip = request.META['REMOTE_ADDR']
    print("访问IP：" + user_ip)
    return render(request,'kdapptest/static_test.html') 

# 显示上传图片页面
def show_upload(request):
    return render(request,'kdapptest/upload_pic.html')