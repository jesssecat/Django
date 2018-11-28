from django.conf.urls import url
from django.contrib import admin
from app01 import views
#这个页面是自己创建的，app01的子路由
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^biaodan/', views.biaodan),
    url(r'^user_list', views.user_list),
    url(r'^user_add', views.user_add),
    url(r'^user_del', views.user_del),
    url(r'^user_edit', views.user_edit),
    url(r'^book_list', views.book_list),
    url(r'^book_add', views.book_add),
    url(r'^chuban_add', views.chuban_add),
    url(r'^book_del', views.book_del),
    url(r'^book_modifys', views.book_modifys),
    url(r'^tpl_a', views.tpl_a),
    url(r'^tpl_b', views.tpl_b),
    url(r'^upload', views.upload),
    url(r'^json_data', views.json_test),
    url(r'^url/[0-9]{2,4}/$', views.url),#http://127.0.0.1:8000/url/99/
    #url(r'^url/[0-9]{2,4}/[a-zA-Z]{2,4}/$', views.url),#http://127.0.0.1:8000/url/2222/bb/
    url(r'^url/([0-9]{2,4})/([a-zA-Z]{2,4})/$', views.url),  # http://127.0.0.1:8000/url/2222/bb/
    # arg1: 2222 可以给路由传值
    # arg2: bb

]
