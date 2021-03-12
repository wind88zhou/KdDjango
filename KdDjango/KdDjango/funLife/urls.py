from django.urls import path,re_path 
from django.conf.urls import url
from funLife import views # 从自己的 app 目录引入 views

urlpatterns = [ 
    url(r'^funlife$', views.funlife,name='funlife'),
    url(r'^showtep$', views.showtep,name='showtep'),
    url(r'^addapi$', views.addapi,name='addapi'),
    url(r'^index$', views.index,name='index'),
    url(r'^home$',views.home,name='home'),
    url(r'^resultShow$',views.resultShow,name='resultShow'),
    url(r'^htmlstudy$',views.htmlstudy,name='htmlstudy'),
    url(r'^mainpage$',views.mainpage,name='mainpage'),
    url(r'^css_study$',views.css_study,name='css_study'),
    url(r'^form_study$',views.form_study,name='form_study'),
    url(r'^box_model_study$',views.box_model_study,name='box_model_study'),
    url(r'^js_study$',views.js_study,name='js_study'),
    
]



