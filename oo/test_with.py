#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 21:13
# @Author  : ChenYao
# @File    : test_with.py

'''
想让一个类具有上下文管理器功能，需要定义两个魔法函数__enter__,__exit__
'''

# 上下文管理器协议
class Sample:
    # 获取资源
    def __enter__(self):
        print("enter")
        return self   #  必须有

    # 释放资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("do something.")


with Sample() as sample:
    sample.do_something()