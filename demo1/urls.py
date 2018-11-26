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
from django.conf.urls import url
from django.contrib import admin

from app01 import views
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

]
