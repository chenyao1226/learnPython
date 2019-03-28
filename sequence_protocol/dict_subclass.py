#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 17:40
# @Author  : ChenYao
# @File    : dict_subclass.py

'''
dict的子类
'''

'''
不建议继承list和dict
'''

class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

# my_dict = Mydict(one=1)
# my_dict["one"] = 1
# print (my_dict)

'''
如果想要继承dict类型的话，可以继承collections中的UserDict
'''
from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
# my_dict["one"] = 1
print (my_dict)

'''defaultdict
    1. 和dict相比，访问一个不存在的key的时候不会报错
    2. defaultdict初始化的时候支持传递一个类型(list, dict, set, tuple)，以空的该类型作为默认值
    3. defaultdict初始化的时候支持传递一个函数，以这个函数的返回值作为默认参数
'''

from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["bobby"]


for k, v in my_dict.items():
    print(k, v)
