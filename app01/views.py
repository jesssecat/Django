#数据表对应了类
#数据库表中的每一个字段对应类的每一个属性
#数据表中的一条记录对应类的一个实例化对象
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
# Create your views here.
def login(request):
    return render(request,"login.html")
def jesse(request):
    return HttpResponse('hello,word')
def biaodan(request):
    #打印出所有的值
    print(request.POST)
    name = request.POST.get("username",None)
    pwd = request.POST.get("password",None)
    error_msg = ""
    if name == 'jesse' and pwd == '123':
        # return HttpResponse("登录成功")
        return redirect("http://baidu.com")
    else:
        error_msg = "邮箱或者密码错误"
    # print(name, pwd)
    # return render(request, "user_edit.html", {"error": error_msg})

    # return HttpResponse("yes")

def user_list(request):
    #去数据库中查询所有的用户
    #利用ORM这个工具查询数据库不用自己查
    ret = models.UserInfo.objects.all().order_by("id")
    print(ret[0].id, ret[0].name)
    return render(request,"user_list.html",{"user_list":ret})
    # return HttpResponse("请查看输出")

#用户添加
def user_add(request):
    if request.method == "POST":
        new_name = request.POST.get("username",None)
        #去数据库中创建一条用户记录
        models.UserInfo.objects.create(name=new_name)
        return redirect("/user_list/")
    return render(request,"user_add.html")
#用户删除
def user_del(request):
    del_id = request.GET.get("id", None)
    if del_id:
        # del_obj = models.UserInfo.objects.get(id=del_id).delete() #方法一
        del_obj = models.UserInfo.objects.get(id=del_id)
        #删除
        del_obj.delete()
        return redirect("/user_list/")
    else:
        return HttpResponse("要删除的数据不存在！")

def user_edit(request):
    if request.method == "POST":
        print(request.POST)
        edit_id = request.POST.get("id")
        # print(edit_id)
        new_name = request.POST.get("user_name")
        print(new_name)
        if edit_id:
            edit_user = models.UserInfo.objects.get(id=edit_id)
            edit_user.name = new_name
            edit_user.save()
            return redirect("/user_list/")
        else:
            return HttpResponse("用户名不存在!")
    edit_id = request.GET.get("id")
    if edit_id:
        edit_obj = models.UserInfo.objects.get(id=edit_id)
        return render(request, "user_edit.html", {"edit":edit_obj})
    else:
        return HttpResponse("编辑的名称不存在")

#书籍展示相关
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"all_book":all_book})

#书籍添加
def book_add(request):
    ret = models.Chuban.objects.all().order_by("id")
        # models.Book.objects.create(title=book_name)
    if request.method == "POST":
        book_name = request.POST.get("book_name", None)
        chuban_name = request.POST.get("chuban_name", None)
        print(book_name, chuban_name)
        models.Book.objects.create(title=book_name, chuban_id=chuban_name)
        return redirect("/book_list/")
    else:
        print("321")
        return render(request, "book_add.html", {"chuban_list": ret})
    # if request.method == "POST":
    # models.Book.objects.create(title=book_name)
#出版社添加
def chuban_add(request):
    if request.method == "POST":
        new_name = request.POST.get("chuban_name", None)
        print(new_name)
        #去数据库中创建一条用户记录
        models.Chuban.objects.create(name=new_name)
        return redirect("/book_list/")
    return render(request, "chuban_list.html")
#书籍删除
def book_del(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.Book.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/book_list/")
    else:
        return HttpResponse("要删除的数据不存在！")
    return redirect("http://baidu.com")
def book_modifys(request):
    edit_id = request.GET.get("id")
    edit_pid = request.POST.get("id")
    book_name = request.POST.get("book_name")
    chuban_name = request.POST.get("chuban_name")
    if request.method == "GET":
        edit_id = models.Book.objects.get(id=edit_id)
        print(edit_id.title)
        print(book_name)
        print(edit_id)
        # all_book = models.Book.objects.all()
        ret = models.Chuban.objects.all().order_by("id")
        return render(request, "book_modifys.html", {"book_name": edit_id.title, "chuban_list":ret, "edit_id": edit_id})
    else:
        print(edit_pid, book_name, chuban_name)
        edit_book = models.Book.objects.get(id=edit_pid)
        edit_book.title = book_name
        edit_book.chuban_id = chuban_name
        edit_book.save()
        return redirect("/book_list/")