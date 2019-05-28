#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 22:29
# @Author  : ChenYao
# @File    : splice_str.py

'''将多个小字符串拼接
1. 使用for循环将每个字符+在一起，但是这种方式性能太低
2. 使用join方法
'''

s1 = "abc"
s2 = 123
s3 = "efg"

'''
join的参数支持的是迭代器，而不仅仅是列表(list),所以我们使用(str(x) for x in [s1, s2, s3])而不是[str(x) for x in [s1, s2, s3]]
生成器的开销要比列表的开销小得多
'''
ll = "".join((str(x) for x in [s1, s2, s3]))
print(ll)