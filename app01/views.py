#数据表对应了类
#数据库表中的每一个字段对应类的每一个属性
#数据表中的一条记录对应类的一个实例化对象
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
# Create your views here.
from django.shortcuts import render, HttpResponse
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
    return render(request, "book_list2.html", {"all_book":all_book})

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
        print(edit_id.chuban_id)
        print(book_name)
        print(edit_id)
        # all_book = models.Book.objects.all()
        ret = models.Chuban.objects.all().order_by("id")
        return render(request, "book_modifys.html", {"book_name": edit_id.title, "chuban_list":ret, "edit_id": edit_id, "edit_id.chuban_id":edit_id.chuban_id})
    else:
        print(edit_pid, book_name, chuban_name)
        edit_book = models.Book.objects.get(id=edit_pid)
        edit_book.title = book_name
        edit_book.chuban_id = chuban_name
        edit_book.save()
        return redirect("/book_list/")

#测试向前台批量传值
def tpl_a(request):
    data = ["第{:0>3}台服务器".format(i) for i in range(1, 11)]
    return render(request, "tpl_a.html", {"results": data})

def tpl_b(request):
    return render(request, "tpl_b.html")

#文件上传
def upload(request):
    """
       保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
       但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
       :param request:
       :return:
       """
    if request.method == "POST":
        print(request.FILES)
        print(request.FILES["upload_file"].name)
        # print(request.FILES.get("upload_file2").name)
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["upload_file"].name
        # # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
        #     # 从上传的文件对象中一点一点读
            for chunk in request.FILES["upload_file"].chunks():
        #         # 写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")

#json 相关
def json_test(request):
    data = {"name": "jesse", "age":20}
    data2 = [11, 22, 33, 44]
    #备注：原生方法可以，但是django导入的方法不能
    # import json
    # data_str = json.dumps(data2)
    # return HttpResponse(data_str)

    from django.http import JsonResponse
    return JsonResponse(data)
    #{"name": "jesse", "age": 20}

def url(request, arg1, arg2):
    print("arg1:", arg1)
    print("arg2:", arg2)
    return HttpResponse("hello！")
    #http://127.0.0.1:8000/url/2222/bb/
    # arg1: 2222
    # arg2: bb

#书籍分页
def book_page(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 判断用户输入的是否是数字，异常处理
    try:
        page_num = int(page_num)
    except Exception as e:
        page_num = 1
    page_num = int(page_num)
    print(page_num, type(page_num))
    data_start = (page_num-1)*10
    data_end = page_num*10
    per_page = 10 #显示的数量
    #页面上总共展示多少页码
    max_page = 11
    #页面上展示的页码从哪里开始
    total_count = models.Book.objects.all().count()
    total_page, m = divmod(total_count, per_page)
    if m:
        total_page += 1
    if total_page < max_page:
        max_page = total_page
    half_max_page = max_page // 2
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page
    #如果当前页面减一半，比一还小
    if page_start <= 1:
        page_start = 1
        page_end = max_page
    #如果当前页面加一半比总页码数还大
    if page_end >total_page:
        page_end = total_page
        page_start = total_page - max_page +1
    if page_end > total_page:
        page_end = total_page
        page_start = total_page - max_page
    # #总数量
    # #一个需要多少页码
    all_book = models.Book.objects.all()[data_start:data_end]
    #print(total_page)
    # #拼接html
    html_str_list = []
    html_str_list.append('<li><a href="/app01/book_page/?page=1">首页</a></li>')
    if page_num <= 1:
        html_str_list.append('<li style="display:none"><a href="/app01/book_page/?page={}">上一页</a></li>'.format(total_page))
    else:
        html_str_list.append('<li><a href="/app01/book_page/?page={}">上一页</a></li>'.format(page_num -1))
    for i in range(page_start, page_end+1):
        #根据样式判断当前页面
        if i == page_num:
            tmp = '<li><b><a href="/app01/book_page/?page={0}">{0}</a></b></li>'.format(i)
        else:
            tmp = '<li><a href="/app01/book_page/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)
    if page_num >= total_page:
        html_str_list.append('<li style="display:none"><a href="/app01/book_page/?page={}">下一页</a></li>'.format(total_page))
    else:
        html_str_list.append('<li><a href="/app01/book_page/?page={}">下一页</a></li>'.format(page_num +1))
    html_str_list.append('<li><a href="/app01/book_page/?page={}">尾页</a></li>'.format(total_page))
    page_html = "".join(html_str_list)

    #添加一些随机书
    # for i in range(1000):
    #     i = str(i)
    #     i = "新书发布" + i
    #     print(i)
    #     models.Book.objects.create(title=i, chuban_id=1)
    # 添加一些随机书结束
    return render(request, "book_page.html", {"all_book": all_book, "page_html": page_html})

#ajax
def ajax_add(request):
    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    ret = i1 + i2
    print(ret)
    #return HttpResponse(ret, safe=False)
    return HttpResponse(ret)

def ajax_demo1(request):
    return render(request, "ajax_add.html")
#ajax

#json
def json_demo(request):
    # ret = models.Person.objects.all()

    #json的第一种方法
    # persons_list = []
    # for i in ret:
    #     persons_list.append({"name": i.name, "age": i.age})
    # print(persons_list)
    # import json
    # str1 = json.dumps(persons_list)
    # print(str1)
    # return HttpResponse(str1)
    #这样就可以把json传给前台

#json的第二种方法
    ret = models.Person.objects.all()
    from django.core import serializers
    s = serializers.serialize("json", ret)
    print(s)
    return HttpResponse(s)

#json_demo
def persons_demo(request):
    ret = models.Person.objects.all()

    # person_list = []
    # for i in ret:
    #     person_list.append({"name": i.name, "age": i.age})
    # print(person_list)
    # import json
    # s = json.dumps(person_list)
    # print(s)

    # from django.core import serializers
    # s = serializers.serialize("json", ret)
    # print(s)
    # return HttpResponse(s)

    return render(request, "sweetalert_demo.html", {"persons": ret})


def delete_demo(request):
    import time
    time.sleep(3)
    del_id = request.POST.get("id")
    models.Person.objects.filter(id=del_id).delete()
    return HttpResponse("删除成功！")

#判断是否登录，登录则登录成功，否则登录失败
from django.contrib import auth   #使用的自带的auth模块
from django.contrib.auth.decorators import login_required

from app01 import models
from functools import wraps
def check_login(f):
    """
    login_l 方法的session判断是否登录
    request.session["is_login"] = "1"
    如果不等于1，就返回登录页面
    """
    @wraps(f)
    def inner(request, *args, **kwargs):
        if request.session.get("is_login") == "1":
            return f(request, *args, **kwargs)
        else:
            return redirect("/app01/login_l/")
    return inner
def login_1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = models.UserInfo.objects.filter(name=username, password=password)  # [User Obj, ]
        if user:
            # 登陆成功
            request.session["is_login"] = "1"
            request.session["user_id"] = user[0].id
            # 1. 生成特殊的字符串
            # 2. 特殊字符串当成key,在数据库的session表中对应一个session value
            # 3. 在响应中向浏览器写了一个Cookie Cookie的值就是 特殊的字符串

            return redirect("/app01/login_y/")

    return render(request, "login_l.html")
#开始使用装饰器
@check_login
def login_y(request):
    user_id = request.session.get("user_id")
    #根据id去数据库中查找用户
    user_obj = models.UserInfo.objects.filter(id=user_id)
    if user_obj:
        return render(request, "login_y.html", {"user": user_obj[0]})
    else:
        return render(request, "login_y.html", {"user": "匿名用户"})

def logout(request):
    auth.logout(request)
    return redirect("/app01/login_l/")