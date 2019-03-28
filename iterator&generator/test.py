#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 18:45
# @Author  : ChenYao
# @File    : test.py

def gen_func():
    result = yield
    print("result: {}".format(result))
    yield 2
    yield 3


gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))