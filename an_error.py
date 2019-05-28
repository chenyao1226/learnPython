#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 13:58
# @Author  : ChenYao
# @File    : an_error.py


def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
        print(id(self.staffs))

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    com1 = Company("com1", ["bobby1", "bobby2"])
    com1.add("bobby3")
    com1.remove("bobby1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("bobby")
    print(com2.staffs)
    #
    print(Company.__init__.__defaults__)
    #
    com3 = Company("com3")
    com3.add("bobby5")
    print(com2.staffs)
    print(com3.staffs)
    # print(com2.staffs is com3.staffs)

    # a = 1
    # b = 2
    #
    # a = [1,2]
    # b = [3,4]
    #
    # a = (1, 2)
    # b = (3, 4)
    #
    # c = add(a, b)
    #
    # print(c)
    # print(a, b)


'''
一切皆对象
可变对象：
        set list dict
不可变对象：
        int str tuple frozenset float boolean
        
当一个对象被引用时，如果它是可变对象：则每次调用的其实是同一个对象（内存地址相同）
当一个对象被引用时，如果它是不可变对象：则每次调用的是不同的对象（原先对象的副本，彼此之间没有关系）

如果一个可变对象被作为了一个函数的默认参数：以后每次调用这个函数，其实都是对这个默认参数对象进行操作。比如：
        def test(l=[]):
            l.append(1)
        
        调用这个test函数之后，会创建一个空列表对象(默认参数)，以后每次调用这个函数都会基于这个空列表对象进行操作
'''