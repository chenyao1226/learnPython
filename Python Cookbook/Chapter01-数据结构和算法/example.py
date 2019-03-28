#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 14:19
# @Author  : ChenYao
# @File    : example.py

'''
解压序列赋值给多个变量
'''
l = [1, 2, 3, (4,5)]
_, a, b, _ =  l
print(a)
l = [1, 2, 3, (4,5)]
_, a, b, (c, d) =  l
print(c)
'''
需要变量的数目和序列中值的数目一样，否则就会报ValueError错误，我们可以通过星号表达式解决这一问题
'''
l = [1, 2, 3, (4,5)]
a, *_, b =  l
print(a, b)
'''
*在迭代元素是可变长序列的时候是很有用的
'''
l  = [
    ("foo", 1),
    ("bar", 1, 2),
]

for tag, *args in l:
    if tag == "foo":
        print(args)
    elif tag == "bar":
        print(args)
'''字符串分割'''
url = "https://record.zhanqit.tv/fdsfasfa/13154563/15545.m3u8"
*_, filename = url.split("/")
print(filename)