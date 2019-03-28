#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 21:55
# @Author  : ChenYao
# @File    : instance_type.py
'''type和isinstance区别
'''


class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A))
print(isinstance(b, B))

print(type(b) is B)
print(type(b) is A)
'''
    1. isinstance会沿着类的继承链一直查找，只要能找到就会返回True
    2. type会得到类的类似于ID的东西然后进行比较
'''

''' is 和==的区别
    is 比较的是两个对象在内存中的id， ==比较的是两个对象的值
    
'''