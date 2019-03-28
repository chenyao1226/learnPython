#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 9:34
# @Author  : ChenYao
# @File    : learn_exception.py
import time


# 可以给自己的定义的异常再添加一个信息error
class MyException(Exception):
    def __init__(self, error, msg):
        super(MyException, self).__init__(msg)
        self.error = error


try:
    print(10/0)
except Exception as ex:
    raise MyException("计算异常", ex)
