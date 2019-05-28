#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 22:04
# @Author  : ChenYao
# @File    : class_var.py

'''类变量和实例变量
    1. 类变量可以通过类直接访问
    2. 类变量是所有实例共享的
    3. 通过类修改类变量会影响所有实例对该类变量的访问
    4. 通过实例修改类变量只会影响该实例对该类变量的访问，不会影响其他实例的访问
'''


class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
print(a.aa, a.x, a.y)
A.aa = 11
print(a.aa, a.x, a.y)
a.aa = 100
print(A.aa, a.aa, a.x, a.y)
