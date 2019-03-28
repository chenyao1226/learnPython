#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 0:35
# @Author  : ChenYao
# @File    : sort_dict.py
from random import randint
d = {x: randint(60, 100) for x in "abcxyz"}

'''
根据字典中某个值的大小进行排序
'''
# 方式1 zip+sorted
d1 = zip(d.itervalues(), d.iterkeys())
print d
print d1
print sorted(d1)

# 方式2
print sorted(d.iteritems(), key=lambda x: [1])
