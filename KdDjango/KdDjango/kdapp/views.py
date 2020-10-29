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
    