#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : fly
# @File    : urls.py
from django.conf.urls import url
from .views import *
from django.urls import path,re_path

'''
2.0版本中的路由系统已经替换成path
'''
urlpatterns = [
    url(r'^login',login),
    url(r'^user_list',user_list),
    url(r'^add_user',add_user),
    # 出版社
    url(r'^publisher_list',publisher_list,name='pub_l'),  #  起别名,可以做到反向解析
    url(r'^add_publisher',add_publisher,name='ad_pub'),
    url(r'^delete_publisher/(\d+)',delete_publisher,name='de_pub'),
    url(r'^edit_publisher/(\d+)',edit_publisher,name='ed_pub'),
    # 书籍
    url(r'^book_list',book_list,name='book_l'),
    url(r'^add_book',add_book,name='ad_book'),
    url(r'^delete_book/(\d+)',delete_book,name='de_book'),
    url(r'^edit_book/(\d+)',edit_book1,name='ed_book'),
    url(r'^book_search',book_search),
    # 作者
    url(r'^author_list',author_list,name='author_l'),
    url(r'^add_author',add_author,name='ad_author'),
    url(r'^delete_author/(\d+)',delete_author,name='de_author'),
    # url(r'^edit_author',edit_author),
    url(r'^edit_author/(\d+)',EditAuthor.as_view(),name='ed_author'),  # 调用 视图类,要as_view()


    url(r'^test1/$',test),
    # path('test1',test), # 要捕获一段url中的值，需要使用尖括号，而不是之前的圆括号；
                        #  path('articles/<int:year>/', views.year_archive),
    # re_path('^test1',test),
    url(r'^upload',UploadFile.as_view()),
]

