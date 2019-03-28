#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 11:29
# @Author  : ChenYao
# @File    : gencomps.py

'''生成器表达式'''

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = tuple((color, size) for color in colors for size in sizes)
print(tshirts)
for item in ((color, size) for color in colors for size in sizes):
    print(item)
