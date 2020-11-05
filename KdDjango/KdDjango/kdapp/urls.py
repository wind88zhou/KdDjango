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
    url(r'^set_cookie$', views.set_cookie,name='set_cookie'), # 设置cookie
    url(r'^get_cookie$', views.get_cookie,name='get_cookie'), # 获取cookie
    url(r'^set_session$', views.set_session,name='set_session'), # 设置session
    url(r'^get_session$', views.get_session,name='get_session'), # 获取session
    url(r'^clear_session$', views.clear_session,name='clear_session'), # 清除session
]
