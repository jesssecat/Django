from django import template
register = template.Library()

@register.inclusion_tag("ul.html")
def show_ul(num):
    num = 1 if num < 1 else int(num)
    data = ["第{:0>3}台服务器".format(i) for i in range(1, num)]
    return {"data": data}

@register.inclusion_tag('book_list.html')
def show_results(n):
    n = 1 if n < 1 else init(n)
    data = ["第{}项".format(i) for i in range(1, n+1)]
    return {"results":data}

@register.simple_tag(name="yimi")
def my_sum(arg1, arg2, arg3):
    return "{} {} {}".format(arg1, arg2, arg3)