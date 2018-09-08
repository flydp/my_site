#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : fly
# @File    : mypage.py


class Page():
    def __init__(self, page_num, total_count, url_prefix, search, per_page=5, max_page=11):
        """
        自定义分页
        :param page_num: 当前页码数
        :param total_count: 数据总数
        :param url_prefix: a标签href的前缀
        :param per_page: 每页显示多少条数据
        :param max_page: 页面上最多显示几个页码
        :param search: 搜索时的关键字
        """
        self.page_num = page_num
        self.url_prefix = url_prefix
        self.max_page = max_page
        self.per_page = per_page
        self.total_count = total_count
        self.search = search

        total_page, m = divmod(self.total_count, self.per_page)
        if m:
            total_page += 1
        self.total_page = total_page

        if not self.page_num:
            self.page_num = 1
        try:
            self.page_num = int(self.page_num)
        except Exception as e:
            self.page_num = 1
        if self.page_num > total_page:
            self.page_num = total_page
        if self.page_num < 1:
            self.page_num = 1

        # 页面总共展示多少页
        if total_page < self.max_page:
            self.max_page = total_page
        half_max_page = self.max_page // 2

        self.page_start = self.page_num - half_max_page
        self.page_end = self.page_num + half_max_page

        if self.page_start <= 1:
            self.page_start = 1
            self.page_end = self.max_page
        if self.page_end >= total_page:
            self.page_end = total_page
            self.page_start = total_page - self.max_page + 1

        self.data_start = (self.page_num - 1) * self.per_page
        self.data_end = self.page_num * self.per_page

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end

    def page_html(self):
        html_str_list = []
        # 首页
        html_str_list.append('<li><a href="{}?page=1&q={}">首页</a></li>'.format(self.url_prefix,self.search))
        # 上一页
        if self.page_num <= 1:
            html_str_list.append(
                '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            html_str_list.append(
                '<li><a href="{}?page={}&q={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.url_prefix,self.page_num - 1,self.search))

        for i in range(self.page_start, self.page_end + 1):
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}&q={2}">{1}</a></li>'.format(self.url_prefix,i,self.search)
            else:
                tmp = '<li><a href="{0}?page={1}&q={2}">{1}</a></li>'.format(self.url_prefix,i,self.search)
            html_str_list.append(tmp)
        # 下一页
        if self.page_num >= self.total_page:
            html_str_list.append(
                '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_str_list.append(
                '<li><a href="{}?page={}&q={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix,self.page_num + 1,self.search))

        # 尾页
        html_str_list.append('<li><a href="{}?page={}&q={}">尾页</a></li>'.format(self.url_prefix,self.total_page,self.search))
        page_html = ''.join(html_str_list)

        return page_html
