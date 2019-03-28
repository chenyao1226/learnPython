#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 1:39
# @Author  : ChenYao
# @File    : filter_list.py

# 如何在列表，字典，集合中根据条件筛选数据

from random import randint


'''
筛选出一个列表中大于等于0的值
'''

# 先生成一个随机的列表
l = [randint(-10, 10) for _ in range(10)]

# 方式1
l1 = filter(lambda x: x >= 0, l)
# 方式2
l1 = [x for x in l if x >= 0]

'''
筛选出字典中值大于80的item
'''
# 先生成一个字典
d = {x: randint(60, 100) for x in range(1, 20)}
d1 = {k: v for k, v in d.iteritems() if v > 90}


'''
筛选出集合中能被3整除的值
'''
s = set(l)
s1 = {x for x in s if x % 3 == 0}