#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 23:15
# @Author  : ChenYao
# @File    : self_ex.py
'''
python中的自省机制
自省是通过一定的机制查询到对象的内部结构
通过__dict__方法可以查看到对象和类内部的一些结构
dir()也可以实现类似的功能
'''

class Person:
    name = '中国人'

class Student:
    country = "china"
    def __init__(self, school_name):
        self.shcool_name = school_name

stu = Student("北京四中")
print(stu.__dict__)
# stu.__dict__["school_addr"] = "北京市"
# print(stu.__dict__)
#
# print(Student.__dict__)
# print(Person.__dict__)
