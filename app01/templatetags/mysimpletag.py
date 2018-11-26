from django import template
register = template.Library()

@register.simple_tag(name="yimi")
def my_sum(arg1, arg2, arg3):
    return "{} {} {}".format(arg1, arg2, arg3)