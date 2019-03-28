#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 16:59
# @Author  : ChenYao
# @File    : listcomps.py

'''
1. 列表推导在py2中有变量泄露的问题,在py3中则不会
'''

x = 'my precious'
dummy = [x for x in 'ABC']
print(x)
'''
py2中x将会是C
py3中x是my precious
'''

'''
2. 一个推导式中可以有多个for循环
'''
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

