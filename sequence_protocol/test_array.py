#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 22:48
# @Author  : ChenYao
# @File    : test_array.py
'''
array的性能比list要高很多
能用array最好用array
'''


# array, deque
# 数组
import array
#array和list的一个重要区别， array只能存放指定的数据类型
my_array = array.array("i")
my_array.append(1)
my_array.append("abc")
