#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 23:01
# @Author  : ChenYao
# @File    : private_method.py
'''
python中的私有属性
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
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)


'''
    给Person类传递一个Date类型的数据作为birthday
'''


class Person:
    def __init__(self, birthday):
        self.birthday = birthday

    def get_age(self):
        return 2018 - self.birthday.year


p = Person(Date(1993, 1, 18))
print(p.get_age())
print(p.birthday)

'''
    上面的方法是可以访问person的birthday，现在希望把它隐藏起来，不让访问
'''


class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


p = Person(Date(1993, 1, 18))
print(p.get_age())
# print(p.birthday)  # 将会报错

'''
其实还是有方法访问到私有属性的
'''


class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


p = Person(Date(1993, 1, 18))
print(p.get_age())
print(p._Person__birthday)  # 通过这种方法访问私有属性，其实就是做了一个变形
