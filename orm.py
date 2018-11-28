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

#单表查询之神奇的双下划线
# models.Book.objects.filter(id__lt=10, id__gt=1)  # 获取id大于1 且 小于10的值
#
# models.Book.objects.filter(id__in=[11, 22, 33])  # 获取id等于11、22、33的数据
# models.Book.objects.exclude(id__in=[11, 22, 33])  # not in
#
# models.Book.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
# models.Book.objects.filter(name__icontains="ven")  # icontains大小写不敏感
#
# models.Book.objects.filter(id__range=[1, 3])  # id范围是1到3的，等价于SQL的bettwen and
#
# 类似的还有：startswith，istartswith, endswith, iendswith　


#外建的查询操作
#正向查询
#第一种办法
book_obj = models.Book.objects.all().first()
ret = book_obj.chuban #出版是另外一个表，这个表名不用大写
# print(ret, type(ret))#我是一个出版社：测试出版  #obj
# ret = book_obj.chuban.name
# print(ret, type(ret)) #str

#第二种办法
#利用双下划线进行跨表查询
#查询id为1的书的出版社名称
#双下划线跨表查询夸了一个表
ret = models.Book.objects.filter(id=2).values("chuban__name")
# print(ret)


#反向查询
#将出版社出版的书查询出来
chuban_obj = models.Chuban.objects.first()
ret = chuban_obj.book_set.all()
# print(ret)

#根据出版社的ID查询出所出版的书籍
#查询出版社id为1，书的名称
ret = models.Chuban.objects.filter(id=1).values_list("book__title")
print(ret)