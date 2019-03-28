#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:49
# @Author  : ChenYao
# @File    : attr_desc.py
import numbers

'''属性以及属性描述符
'''

'''
有一个Movie类，这个类有一个score的属性
'''
class Movie:
    def __init__(self, title, description, score, ticket):
        self.title = title
        self.score = score
        self.description = description
        self.ticket = ticket

'''
设计完这个类之后，忽然发现Movie中的score属性不能为负的，所以需要对它进行一些约束，于是重新设计
'''

class Movie:
    def __init__(self, title, description, score, ticket):
        self.title = title
        if score < 0:
            raise ValueError("positive value need")
        self.score = score
        self.description = description
        self.ticket = ticket
'''
但是这样不行，这样只会在Movie初始化的时候对score进行约束，对于已经存在的实例就无能为力了，因为通过实例依然可以修改score属性
这时候可以使用property
通过设置属性的getter, setter, deletter方法我们可以在任何地方对它进行约束
'''

class Movie:
    def __init__(self, title, score, ticket, desc):
        self.title = title
        self.score = score
        self.ticket = ticket
        self.desc = desc

    @property
    def score(self):
        pass
        # return self._score   # 如果这里有返回值的话，就不需要@score.getter了，@score.getter的优先级大于这里的

    @score.getter
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("positive value need")
        self._score = score

    @score.deleter
    def score(self):
        raise AttributeError("Can not delete")

'''
如果也需要对ticket（票数）进行约束，那就也需要对它设置为属性，并规定setter方法，有没有一种通用的方式？
这时候就可以用属性描述符
        1. 将某种特殊类型的类的实例指派给另一个类的属性，而这种特殊类型的类就是实现了
        __get__，__set__,__delete__的新式类，只要实现了这三种方法中任意一种就是描述符类
        2. 描述符会改变一个属性的获取，设置，删除的方式
'''
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        pass


class Movie:
    socre = Integer("score")
    ticket = Integer("ticket")

    def __init__(self, title, score, ticket, desc):
        self.title = title
        self.score = score
        self.ticket = ticket
        self.desc = desc

m = Movie("", -1, -1, "")
print(m.score)
print(m.ticket)

'''
上面的代码实现了代码重用，但是问题来了：__init__方法中的score和ticket是怎么和类属性score，ticket联系起来的呢？
    如果m是某个类的实例，那么m.score（以及等价的getattr(m,’score’)）
    首先调用__getattribute__。如果类定义了__getattr__方法，
    那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
    而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。

     m = movie(), m.score查找顺序如下：
    （1）如果“score”是出现在Movie或其基类的__dict__中， 且m是data descriptor， 那么调用其__get__方法, 否则
    （2）如果“score”出现在m的__dict__中， 那么直接返回 obj.__dict__[‘score’]， 否则
    （3）如果“score”出现在Movie或其基类的__dict__中
        （3.1）如果score是non-data descriptor，那么调用其__get__方法， 否则
        （3.2）返回 __dict__[‘score’]
    （4）如果User有__getattr__方法，调用__getattr__方法，否则
    （5）抛出AttributeError

就是查找类本身的__dict__的优先级要高于查找对象本身的__dict__
'''