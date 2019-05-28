#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 1:07
# @Author  : ChenYao
# @File    : find_dict_public_key.py
from random import randint, sample
from functools import reduce
'''
在多个字典中找到公共key
'''

# 先创建字典
d1 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}
d2 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}
d3 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

print(d1)
print(d2)
print(d3)

# 方法1 通常的做法
res = []
for k in d1:
    if k in d2 and k in d3:
        res.append(k)
print(res)

# 方法2  利用集合的交集
print (d1.viewkeys() & d2.viewkeys() & d3.viewkeys())

# 方法3 map+reduce+lambda
print(reduce(lambda a, b: a & b, map(dict.viewkeys, [d1, d2, d3])))