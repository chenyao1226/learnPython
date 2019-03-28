#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/5 20:43
# @Author  : ChenYao
# @File    : python_gil.py

'''gil global interpreter lock （cpython）
    1. python中一个线程对应于c语言中的一个线程
    2. gil使得同一个时刻只有一个线程在一个cpu上执行字节码, 无法将多个线程映射到多个cpu上执行
    3. pypy是去gil的
'''

total = 0

def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global total
    for i in range(1000000):
        total += 1
def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)

'''
通过多次运行代码可以看出来total的值是不稳定的，说明gil在某些条件下是会自己释放的，否则total的值应该是0
    gil会根据执行的字节码行数以及时间片释放gil，gil在遇到io的操作时候主动释放，所以io密集的操作，多线程是适用的
'''