#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : fly
# @File    : mysimpletag.py

'''
# 自定义simple tag
# 比filter更自由化
# register必须这样拼写
'''
from django import template

register = template.Library()


# 三个字符串拼接
@register.simple_tag(name='mySum')
def my_sum(arg1, arg2, arg3):
    return '{}{}{}'.format(arg1, arg2, arg3)

'''
# 自定义inclusion_tag
多用于展示html代码
'''

@register.inclusion_tag('results.html')
def show_results(n):
    n = 1 if n < 1 else int(n)
    data = ['第{:0>3}项'.format(i) for i in range(1,n+1)]
    return {'data':data}