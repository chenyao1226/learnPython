#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 22:20
# @Author  : ChenYao
# @File    : slice_obj.py
'''
1. 根据collection中abc模块知道一个序列协议应该实现哪几种方法
2. 实现切片考的最主要的方法就是__getitem__方法
3. 对列表切片返回的还是列表，所以对我们自定义的类切片返回的也应该是自定义的类
'''


import numbers

class Group:
    #支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ["bobby1", "imooc", "bobby2", "bobby3"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)
reversed(group)
for user in group:
    print(user)