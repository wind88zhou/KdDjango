from django.urls import path, re_path
from django.conf.urls import url
from KdTestApp import views  # 从自己的 app 目录引入 views

urlpatterns = [
    url(r'^mainpage', views.main_page, name='main_page'),
    url(r'^add_pramas', views.add_pramas, name='add_pramas'),
    url(r'^api_list', views.api_list, name='api_list'),
]
