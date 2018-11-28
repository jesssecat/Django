from django.db import models

# Create your models here.
#个人用户添加表
from django.db import models
#ORM相关的只能写在这个文件里面，写到别处文件django找不到
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)#创建一个自增的主键
    name = models.CharField(null=False, max_length=20)#创建一个varchar(20)类型的字段


#出版社和图书编辑表
class Chuban(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False, unique=True)
    def __str__(self):
        return "我是一个出版社：{}".format(self.name)
#书籍
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    chuban = models.ForeignKey(to="Chuban")
    def __str__(self):
        return self.title
        # return "<Book Object:{}>".format(self.title)