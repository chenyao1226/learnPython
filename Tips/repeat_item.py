#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 23:51
# @Author  : ChenYao
# @File    : repeat_item.py


from random import randint
l = [randint(0, 20) for _ in range(30)]

'''
统计一个列表中元素重复次数最高的三个元素
'''
# 方式1
d = dict.fromkeys(l, 0)
for x in l:
    d[x] += 1

print(sorted(d.iteritems(), key=lambda x: x[1]))
# 方式2 colletions.Counter
from collections import Counter

d2 = Counter(d)
print(d2.most_common(3)) # 直接打印重复次数最高的前三个元素