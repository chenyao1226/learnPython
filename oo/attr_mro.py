#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 22:23
# @Author  : ChenYao
# @File    : attr_mro.py
'''在继承中关系中，属性和方法的查找顺序
    1. py2中如果是经典类会使用深度优先算法，如果是新式类(继承object)的话会使用广度优先算法
    3. py3统一为新式类，不管写不写(object)，默认都会继承object，统一使用C3查找算法,通过__mro__方法查看查找顺序

'''


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)


class A1:
    pass


class A2:
    pass


class B(A1):
    pass


class C(A2):
    pass


class D(B, C):
    pass


print(D.__mro__)
