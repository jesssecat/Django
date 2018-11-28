"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app01 import views, urls

urlpatterns = [
    url(r'^app01/', include(urls)),#设置路由，指向到app01的项目下面的子路由，可以做前台和后台
    #url(r'^app01/', include(urls)),#设置路由，指向到app01的项目下面的子路由，可以做前台和后台
    # url(r'^login/', views.login),
    # url(r'^biaodan/', views.biaodan),
    # url(r'^user_list', views.user_list),
    # url(r'^user_add', views.user_add),
    # url(r'^user_del', views.user_del),
    # url(r'^user_edit', views.user_edit),
    # url(r'^book_list', views.book_list),
    # url(r'^book_add', views.book_add),
    # url(r'^chuban_add', views.chuban_add),
    # url(r'^book_del', views.book_del),
    # url(r'^book_modifys', views.book_modifys),
    # url(r'^tpl_a', views.tpl_a),
    # url(r'^tpl_b', views.tpl_b),
    # url(r'^upload', views.upload),
    # url(r'^json_data', views.json_test),
    # url(r'^url/[0-9]{2,4}/$', views.url),#http://127.0.0.1:8000/url/99/
    # #url(r'^url/[0-9]{2,4}/[a-zA-Z]{2,4}/$', views.url),#http://127.0.0.1:8000/url/2222/bb/
    # url(r'^url/([0-9]{2,4})/([a-zA-Z]{2,4})/$', views.url),  # http://127.0.0.1:8000/url/2222/bb/
    # arg1: 2222 可以给路由传值
    # arg2: bb

]
