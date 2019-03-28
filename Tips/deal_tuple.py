#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 23:29
# @Author  : ChenYao
# @File    : deal_tuple.py

# ("jim", 16, "male", "jim8721@gmail.com")
# ("lilie", 17, "male", "lilei@gmail.com")
# ("lucy", 16, "female", "lucy@gmail.com")

student = ("jim", 16, "male", "jim8721@gmail.com")

'''
通常我们访问元祖中的数据的话是这样的
'''

# name
name = student[0]
# age
age = student[1]
# sex
name = student[2]
# mail
mail = student[3]

'''
很多索引（[0],[1],[2]），不利于代码的可读性
'''
# 方式1 定义一系列的常量值
NAME, AGE, SEX, MAIL = range(4)
print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[MAIL])

# 方式2 使用标准库中colletions.namedtuple代替内置tuple
from collections import namedtuple
# 初始化
student = namedtuple("student", ["name", "age", "sex", "mail"])
# 创建命名元组方式1
s = student("jim", 16, "male", "jim8721@gmail.com")
# 创建命名元组方式2
s2 = student(name="jim", age=16, sex="male", mail="jim8721@gmail.com")
# 直接通过属性的方式访问
print(s.name, s2.name)
print (s.sex, s2.sex)
# namedtuple 是tuple的子类
print(isinstance(s, tuple))
