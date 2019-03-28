#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 15:30
# @Author  : ChenYao
# @File    : magic_function.py

'''魔法函数
    魔法函数指的是在我们定义一个类的时候，python自动给我们提供的哪些以双下划线开始，
    双下划线结尾的函数，这些函数可以扩展我们所定义类的功能
'''

# 初识魔法函数
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    # 这个就是魔法函数之一
    def __getitem__(self, item):
        return self.employee[item]

# company = Company(["tom", 'jerry', 'eric'])
# for em in company:
#     print(em)

'''魔法函数之__str__
    使用str函数进行强制类型转换的时候会调用
'''
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ','.join(self.employee)

# company = Company(["tom", 'jerry', 'eric'])
# s = str(company)
# print(s)

'''魔法函数值__repr__
    使用repr函数进行强制类型转换的时候会调用   
'''
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __repr__(self):
        return ','.join(self.employee)

# company = Company(["tom", 'jerry', 'eric'])
# print(repr(company))

'''魔法函数值__len__
    使用len函数进行强制类型转换的时候会调用
'''
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

# company = Company(["tom", 'jerry', 'eric'])
# print(len(company))