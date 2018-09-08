#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : fly
# @File    : myfilter.py


'''
# 第一个参数永远是管道符前面的变量
# 自定义filter  templatetags文件夹名不能错

'''
from django import template


register = template.Library()


@register.filter(name='sb')
def add_sb(arg):
    return '{}sb'.format(arg)


@register.filter(name='addstr')
def add_str(arg,arg2):
    return '{}{}'.format(arg,arg2)