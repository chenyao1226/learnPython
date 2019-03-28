#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 1:33
# @Author  : ChenYao
# @File    : use_dque.py

from random import randint
from collections import deque
import pickle

'''
有个猜数值的游戏，需要记录最近五次猜的数值，并且在程序退出的时候把历史记录存到文件中
'''
N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print("%s is less-than N" % k)
    else:
        print("%s is greater|-than N" % k)
    return False


while True:
    line = input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == "history" or line == "h?":
        print(list(history))
    elif line == "q":
        pickle.dump(history, open("history", "w"))
        break
