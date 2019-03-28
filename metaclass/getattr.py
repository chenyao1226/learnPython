#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:23
# @Author  : ChenYao
# @File    : getattr.py
from datetime import date, datetime
'''py中的两个魔法函数__getattr__和__getattribute__
    1. 访问对象不存在的属性是会报错的，这时候会调用__getattr__方法，如果没有定义__getattr__方法，将会抛出异常，
        否则将会执行这个方法中的逻辑
    2. 只要访问了对象的属性就会调用__getattribute__方法，只要这个方法存在，无论要访问的属性存在与否，都不会报错，
        如果访问了多次或者多个属性将会调用这个方法多次
'''

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    # 当要访问的对象的属性不存在的时候会调用这个方法, 我们可以在这个方法中添加一些自己的逻辑
    def __getattr__(self, item):
        return "attribute not found"

user = Person("eric", date(year=1993, month=1, day=1))

print(user.age)


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


    def __getattribute__(self, item):
        return "你在访问我的属性"

user = Person("eric", date(year=1993, month=1, day=1))

print(user.age)
print(user.name)
