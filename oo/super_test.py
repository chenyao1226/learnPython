#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 11:08
# @Author  : ChenYao
# @File    : super_test.py

'''
py2中调用父类构造方法的方式
'''

# class A:
#     def __init__(self):
#         print("A")
#
# class B(A):
#     def __init__(self):
#         print("B")
#         super(B, self).__init__()
#
# if __name__ == "__main__":
#     b = B()

'''
1. super函数并不是调用父类中的构造方法，而是调用mro中下一个方法
'''


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("C")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == "__main__":
    d = D()
    print(D.__mro__)
