from django.shortcuts import render,redirect #导入简单的重定向函数
from django.http import HttpResponse, JsonResponse,FileResponse,HttpResponseRedirect
from kdapp  import models
from kdapp.models import BookInfo
from kdapp.My_forms import EmpForm
from django.core.exceptions import ValidationError
from datetime import date
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

    return render(request,"login.html")


def longin_check(request):
    '''登录校验视图'''
    # 1、获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2、进行登录校验
    if username == 'smart' and password =='123':
        # 用户名、密码正确
        return redirect('index')
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
    response.set_cookie('num',1)
    # 返回response
    return response

# /get_cookie
def get_cookie(request):
    # 去除cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)