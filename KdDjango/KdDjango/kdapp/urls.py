from django.urls import path,re_path 
from django.conf.urls import url
from kdapp import views # 从自己的 app 目录引入 views

urlpatterns = [ 
    url(r'^showAppMsg$', views.showAppMsg,name='showAppMsg'),
    path('addemp', views.addemp,name='addemp'),  
    # path('linklist', views.linklist,name='linklist'),
    # path('updatelink', views.updatelink,name='updatelink'),
    # path('dellink', views.dellink,name='dellink'),
    url(r'^index$', views.index,name='index'),
    url(r'^create$', views.create,name='create'),
    url(r'^delete(\d+)$', views.delete,name='delete'), # 捕获URL参数：位置参数
    url(r'^login$', views.login,name='login'),
    url(r'^longin_check$', views.longin_check,name='longin_check'),
    url(r'^login_ajax$', views.login_ajax,name='login_ajax'),
]
