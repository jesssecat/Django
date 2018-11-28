# ORM练习测试
# 如何在一个py脚本或者文件中，加载dj项目的配置和变量的信息
import os
if __name__ == '__main__':
#加载dj的配置信息
#demo1为项目的名称
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo1.settings")
    import django
    #启动
    django.setup()
from app01 import models
books = models.Book.objects.all()#查询所有
# print(books)

#get查询
#可以查询id，等字段，缺点就是没有时会报错
ret = models.Book.objects.get(id=7)
# print(ret.title)

#查询id=7
#filter的好处：结果没有时候会输出空，不会报错，他是列表，必须通过索引的方式取出来
#[0].[1]
ret = models.Book.objects.filter(id=17)
# print(ret)
#查询id大于5
ret = models.Book.objects.filter(id__gt=5)
# print(ret)#取出所有的结果集
# print(ret[0])#取出结果集中的第一元素

#exclude 排除
ret = models.Book.objects.exclude(id=2)
# print(ret)

#values 将某一个字段的value值都展示出来
# ret = models.Book.objects.values("chuban_id", "title")
# ret = models.Book.objects.values("title")
# ret = models.Book.objects.values()#这是全部的信息
# print(ret)

#oder_by 排序
ret = models.Book.objects.all().order_by("id")
#reverse()只能在已经排好序的情况下进行倒序，直接倒序不可以
ret1 = models.Book.objects.all().order_by("id").reverse()
# print(ret)
# print(ret1)

#count()
ret = models.Book.objects.all().count()
# print(ret)

#first() 和last()取出第一条和最后一条

