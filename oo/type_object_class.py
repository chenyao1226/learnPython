#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 14:47
# @Author  : ChenYao
# @File    : type_object_class.py

'''type, object和class关系
    弄清楚这三者之间的关系就可以知道为什么python中的一切皆对象
'''

a=1
b='abc'
print(type(1))
print(type(b))
print(type(int))
print(type(str))

'''
通过上面的代码可以知道，所有我们常见的类的所属类型都是type，或者说是type的对象（实例），
'''
class Student:
    pass

print(type(Student))

'''
即使是我们自定义的类他的类型也是type
'''

print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
'''
    所有类的基类（父类）都是object，那么object的是谁的对象呢
'''
print(type(object))
'''
    object的也是type的对象，那么type有是谁的对象呢，它的基类是什么
'''

print(type(type))
print(type.__bases__)
'''
    通过上面的代码可以看到：
        1. type本身是一个类，但同时它又是他自己的对象（实例），这个实现原理利用了c语言中的指针
        2. type的基类是object， 但是object又是type的对象，所以type和object之间是环形的结构，type自己也是一个环形
'''

'''结论
    object，和type是python中最顶级的类，但是同时他们自身也是对象，所以我们可以说python一切皆对象
'''