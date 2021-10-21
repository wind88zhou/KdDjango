# coding=utf-8
from __future__ import division
import pymysql as MySQL
# from django.http import JsonResponse
# import requests
from django.shortcuts import render
from .models import Api_Info
from datetime import datetime


def main_page(request):
    # 数据库连接测试
    print("开始连接ing")
    try:
        conn = MySQL.connect(host="81.71.139.152", port=3306, user="root", passwd="Qq1025121139", db="fun_life",
                             charset='utf8')
    except:
        print("连接失败!")
    print("连接成功！！！")
    return render(request, 'kdtestapp_front/mainpage.html')


def add_pramas(request):
    add_api_info = Api_Info(api_name='nametest', api_url='apiurltest', api_method='methodtest',
                            api_params='api_paramstest', api_dsc='api_dsc', api_creat_time=datetime.now(), api_update_time=datetime.now())
    add_api_info.save()
    print("已保持一条数据至数据库啦！")
    return render(request, 'kdtestapp_front/add_pramas.html')


def api_list(request):
    api_info = list(Api_Info.objects.all().values())
    now = datetime.now()
    return render(request, 'kdtestapp_front/api_list.html', locals())
