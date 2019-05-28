#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 10:52
# @Author  : ChenYao
# @File    : what_is_var.py

'''python中的对象引用
    python和java中的变量本质不一样，python的变量实质上是一个指针，指针大小是固定的，无所谓类型，可以指向任何一种数据类型
'''

a = 1
a = "abc"
# 1. a贴在1上面
# 2. 先生成对象 然后贴便利贴

'''
a和b指向的是同一个对象
'''
a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a is b)
# b.append(4)
# print (a)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

'''
python 中一切皆对象，类也是对象，type方法返回的是一个类，通过is来判断是否和我们要比较的目标对象是不是同一个
'''


class People:
    pass


person = People()
if type(person) is People:
    print("yes")

'''
py中有一种优化机制：
        两个相同值的简单数据类型对象指向的是同一个内存空间        
'''
a = 1
b = 1
print(a == b)
print(id(a), id(b))
print(a is b)
