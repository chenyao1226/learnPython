#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 22:06
# @Author  : ChenYao
# @File    : test_sequence.py

my_list = []
my_list.append(1)
my_list.append("a")

from collections import abc

'''
abc模块中实现了序列的基类，规定序列协议应该实现哪几种方法
'''

'''拼接一个列表四种不同的方式
    1. c = a + b
    2. a += b
    3. a.extend()
    4. a.append
'''

'''

'''
a = [1,2]
c = a + [3,4]

'''这种方法其实是用魔法函数__iadd__
__iadd__方法本质上还是调用的extend方法
'''
a += (3,4)

a.extend(range(3))

a.append((1,2))
print(a)

'''
extend方法支持的参数类型是迭代器，所以+= （列表，元组，集合都是可以的）
'''