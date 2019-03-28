#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:57
# @Author  : ChenYao
# @File    : yield_from.py

from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "cy1","www.baidu.com"
    "cy2","www.xxoo.com"
}

def my_chain(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value

# for value in my_chain(my_list, my_dict, range(5)):
#     print(value)


'''上面的这段代码通过yield from实现'''
def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable


# for value in my_chain(my_list, my_dict, range(5)):
#     print(value)


'''yield from的功能
    1. main 调用方
    2. g1(委托生成器)
    3. gen 子生成器
yield from会在调用方与子生成器之间建立一个双向通道
'''

def gen_func():
    v1 = yield 1
    print(v1)
    v2 = yield 2
    print(v2)
    v3 = yield 3
    print(v3)


def g1(gen):
    yield from gen

def main():
    gen = gen_func()
    g = g1(gen)
    g.send(None)
    g.send(2)
    g.send(3)

main()

