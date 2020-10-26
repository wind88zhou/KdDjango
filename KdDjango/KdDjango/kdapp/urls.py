from django.urls import path,re_path 
from django.conf.urls import url
from kdapp import views # 从自己的 app 目录引入 views

urlpatterns = [ 
    url(r'^showAppMsg$', views.showAppMsg,name='showAppMsg'),
    path('addemp', views.addemp,name='addemp'),  
    # path('linklist', views.linklist,name='linklist'),
    # path('updatelink', views.updatelink,name='updatelink'),
    # path('dellink', views.dellink,name='dellink'),
]
