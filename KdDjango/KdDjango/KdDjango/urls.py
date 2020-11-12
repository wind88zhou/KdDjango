"""KdDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.hello),
# ]

from django.urls import path,include
from django.conf.urls import url
from kdapp import views
from django.contrib import admin 
from . import views
 
urlpatterns = [
    path('hello/', views.hello),
    path('sayNMB/',views.sayNMB),
    path('kdapp/', include('kdapp.urls'),namespace='kadpp'),
    url(r'^admin/', admin.site.urls),
]
