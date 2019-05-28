#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 14:31
# @Author  : ChenYao
# @File    : all_is_object.py

'''python中的一切皆对象
    函数和类也是对象，属于python 的一等公民
    1. 赋值给一个变量
    2. 可以添加到集合对象中
    3. 可以作为参数传递给函数
    4. 可以当作函数的返回值（装饰器的原理）
'''


def ask(name="eric"):
    print(name)


class Person:
    def __init__(self):
        print("alex")


# 赋值给一个变量
my_func1 = ask
my_func1()

my_func2 = Person
my_func2()

# 可以添加到集合对象中
obj_list = list()
obj_list.append(ask)
obj_list.append(Person)

for obj in obj_list:
    print(obj())


def print_type(item):
    print(type(item))


print_type(ask)
print_type(Person)


# 可以当作函数的返回值（装饰器的原理）
def decorator_func():
    print("dec start")
    return ask


my_ask = decorator_func()
my_ask()
