#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 22:32
# @Author  : ChenYao
# @File    : class_method.py
'''静态方法和类方法'''

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)


date = Date(2018, 4, 25)
print(date)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)


'''
假如我们传入的是一个类似于2018-4-25的字符串, 可以加一个静态方法专门处理这种参数
静态方法改变了命名空间
'''
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(year, month, day)

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)

date = Date.parse_from_string("2018-4-25")
print(date)


'''
静态方法的弊端： 在静态方法中调用类是通过指定类名的方式，如果类名改变了就也需要在静态方法中修改这个类名
这个时候就需要类方法了
'''

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @classmethod
    def parse_from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(year, month, day)

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)

date = Date.parse_from_string("2018-4-25")
print(date)

'''那么说静态方法是不是可以完全被类方法取代呢？如果不需要调用类本身，返回的是和类无关的一些内容就应该使用静态方法
'''

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @classmethod
    def is_valid(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and (int(month) >0 and int(month)<=12) and (int(day) >0 and int(day)<=31):
            return True
        else:
            return False

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)

date = Date.is_valid("2018-13-25")
print(date)