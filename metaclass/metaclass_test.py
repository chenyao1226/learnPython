#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 21:48
# @Author  : ChenYao
# @File    : metaclass_test.py

'''通过type创建类
python中一切皆对象，所有的类type的实例，所以type是可以创建类的， 所以先用type创建一个类看看
可以查看type的源码看到type的构造方法都需要传递哪些参数:
    1. 第一个参数是类名
    2. 第二个参数是基类的元组（可以有多个基类,默认都会继承object）
    3. 以字典的形式给类传递属性，不仅可以传递属性还可以传递方法
'''


def say(self):  # 需要带有self参数
    print("hello")


class_obj = type("Person", (), {"name": "eric", "say": say})
p = class_obj()
print(p.name)
p.say()
print(type(class_obj))
print(class_obj.__bases__)
print(class_obj.__dict__)

'''什么是元类？ 元类就是创建类的类，就是指的type，所以编写一个元类的时候要继承type
'''


class UserMetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=UserMetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


'''
进行实例化的时候，会先找metaclass，如果有metaclass，就会通过metaclass创建类对象和实例，本类中没有metaclass就会查找基类的，
如果都找不到就会通过默认的type创建
'''

u = User("eric")
print(u)

'''
元类是用来创建类的，我们使用元类的原因就是要控制创建类的过程，我们可以在这个过程中加入自己的逻辑
'''
