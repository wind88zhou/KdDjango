from django.urls import path,re_path 
from django.conf.urls import url
from funLife import views # 从自己的 app 目录引入 views

urlpatterns = [ 
    url(r'^funlife$', views.funlife,name='funlife'),
    url(r'^showtep$', views.showtep,name='showtep'),
  ]



