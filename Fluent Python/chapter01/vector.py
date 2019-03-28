#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:33
# @Author  : ChenYao
# @File    : vector.py

from math import hypot

'''__abs__
    abs是python中的内置方法，求出绝对值
'''

'''__bool__
    如果一个类定义了__bool__方法，就可以直接进行条件判断
'''

'''__add__和__mul__
    分别用来实现对象加，乘的能力，都是返回一个新的对象，不会改变原来的对象
'''

'''__str__和__repr__
    str()和%s会调用__str__方法
    repr()和%r会调用__repr__方法
    
    如果只想定义这两种方法中的一个，推荐__repr__，如果一个对象没有__str__函数，而python又想要调用它的时候
    解释器会用__repr__作为代替
'''

class Vector:
    '''
    自定义一个数值类型
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" %(self.x, self.y)

    def __abs__(self):
        # hypot 会返回两个值得欧几里得距离，参考勾股定理
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



'''
想len(),abs()这种python的内置方法如果处理的是python内置的数据类型，往往调用的不是魔法函数
而是调用的由c语言实现的特殊方法，因为这样更快，但是为了保证语言的一致性，内置的方法也实现了这些魔法函数
这是python之禅
                不能让特例特殊到开始破坏既定规则
'''