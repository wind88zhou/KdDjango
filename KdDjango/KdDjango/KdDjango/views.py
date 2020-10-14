from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello worl!!#@@d !! ")

def sayNMB(request):
    return HttpResponse("~~~~搜嘎，换个函数功能配置URLS就是实现切换路径切换啊！")