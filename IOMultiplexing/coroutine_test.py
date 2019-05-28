#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 22:32
# @Author  : ChenYao
# @File    : coroutine_test.py

'''什么是协程
'''

'''先伪代码解释一下为什么需要协程
    需求：
        爬取网页有两个步骤：
            1. 根据url获取html内容
            2. 从html中解析出所有的url
        那么问题就来了：
            根据url获取html内容，这个过程会遇到网络IO，肯定时间会比较久，这个时候我们想跳出这个函数的执行，
            转而去执行其他的函数，过了一段时间之后又需要回来继续执行这个函数，那么如何实现暂停一个函数的执行，然后适时的又恢复执行呢？
            这就可以用到协程，而协程的实现原理就是生成器
'''


def get_url(url):
    html = get_html(url)
    # 我想跳出去
    urls = parse_html(html)


def get_url2(url):
    html = get_html(url)
    urls = parse_html(html)
