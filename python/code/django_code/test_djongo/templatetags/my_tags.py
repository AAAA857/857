from django import template



register = template.Library()

@register.filter
def Add(x,y):
    '''
    自定义一个filter方法
    实现俩个数字相乘
    :param x:
    :param y:
    :return:
    '''

    Count = x*y

    return Count

'''
定义自定义标签 全部小写
'''
@register.filter
def lower(value):

    return value.lower()