#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 18:40
# @Author  : ChenYao
# @File    : new_in_py3.py
import time

'''print
py3中打印内容必须使用()
'''

'''input
1. py2中用input和raw_input获取用户输入,py3中统一用input获取用户输入
2. py2中raw_input获取的用户输入统一是str格式的，input如果获取的是数值的话将会是int型，py3中统一是str
'''

'''/ 除法计算
1. py2中用/的计算结果如果有小数将会舍弃小数部分
2. py3中用/将会保留小数部分，用//除将会保留小数部分
'''

'''range
1. py2中range()将会返回一个list类型，py3中返回的是range类，需要用强制类型转换list(range(5))才可以得到一个list
2. range类本身是可迭代的,所以仍然可以使用for x in range(5)
3. py3中舍弃xrange，统一使用range
'''

'''Exception
py3中不支持except Exception, 统一用except Exception as ex
'''

'''filter
py2中使用filter将会获得一个list类型的值，py3中返回的将是filter类，需要用list进行强制类型转换
'''
l = list(range(9))
fl = filter(lambda x:x>5, l)
print(type(fl)), print(fl)
print(list(fl))

'''map
py2中使用map将会获得一个list类型的值，py3中返回的将是map类，需要用list进行强制类型转换
'''

'''迭代器
py2中迭代器都有一个内置的next的方法，py3中变成了__next__
'''

'''文件操作
1. py2中有file和open两种打开文件的方法，py3中统一为open
'''

'''在继承关系中，属性和方法的查找顺序
    1. py2中有新式类（广度优先）和经典类（深度优先）
    2. py3统一是新式类，不管有没有显式写继承object都视为新式类，查找算法为C3，通过__mro__方法可以查看查找顺序
'''