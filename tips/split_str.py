#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 21:41
# @Author  : ChenYao
# @File    : split_str.py
'''
使用多个分割符对一个字符串进行分割
'''

s = "ab;cd|efg|hi,,jkl,|mn\topq;rst,uvw\txyz"
ds = ";,|\t"
# =============================方法一================================
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t
    return [x for x in res if x]  # 去除空字符串

print(mySplit(s, ds))

# ==========================方法二=====================================
import re
ss = re.split(r'[;,|\t]+', s)
print(ss)