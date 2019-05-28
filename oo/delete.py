#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 10:49
# @Author  : ChenYao
# @File    : delete.py

'''py的垃圾回收机制
    1. cpython中的垃圾回收机制的算法是彩妆用引用计数
    2. 魔法函数__del__方法会在对象被回收的时候被执行
'''

a = object()
b = a
del a
print(b)
print(a)


class A:
    def __del__(self):
        pass
