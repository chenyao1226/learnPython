#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 19:58
# @Author  : ChenYao
# @File    : duck_type.py

'''鸭子类型
    当看到一个动物走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子
    对应到下面这段代码，就是：
        如果一个东西会叫（有say方法），那么我们就可以称它为动物，所以，Dog，Cat，Duck都是动物
'''

class Dog(object):
    def say(self):
        print("i am a dog")

class Cat(object):
    def say(self):
        print("i am a cat")

class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Dog, Cat, Duck]

for an in animal_list:
    an().say()

'''python的多态是鸭子类型，看起来好像很鸡肋，其实鸭子类型在python中是一个很重要的理念，在python最初设计的时候就定了这一理念
    这一理念赋予了python灵活，简单的特性，可以通过下面这段代码理解这一理念
'''

a = [1, 2]
b = [3, 4]

s = set()
s.add(5)
s.add(6)

t = {7, 8}
# list类型的extend方法可以扩展元素
a.extend(b)
# 给extend方法传递一个list类型的参数当然没问题，但是通过看源码可以发现其实extend方法支持的是迭代器类型
# 所以可以给extend传递set，tuple等所有的可迭代类型
a.extend(s)
a.extend(t)
print(a)
# 什么是可迭代类型呢？只要类中有__iter__或者__getitem__方法那么这个类就是可迭代的
# 所以自定义一个可迭代的类，传递给extend方法一样没有问题
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(["tom", "jerry"])
a.extend(company)
print(a)

'''结合鸭子模型，__getitem__是魔法函数，几乎所有的类可以都有__getitem__方法，所以他们都相同的一种一种能力，他们都属于某一类的读动态，
    在某个场景下，他们都是通用的，这就是鸭子类型造就了python的灵活性
'''