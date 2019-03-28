#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:07
# @Author  : ChenYao
# @File    : call_test.py

import asyncio

'''loop提供了很多种call方法，call不是以协程的方式调用，而是普通的调用，和call方法配置使用的是loop.run_forever方法
    这个方法不会停止程序，所以需要loop.stop来停止程序
    
        call_soon
        call_later
        call_at
'''

def callback(sleep_times, loop):
    print("success time {}".format(loop.time()))


def stoploop(loop):
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, callback, 2, loop)
    loop.call_later(2, callback, 2, loop)
    loop.call_soon(callback, 4, loop)
    loop.call_soon_threadsafe(callback, loop) # 线程安全的call_soon
    # loop.call_soon(stoploop, loop)
    loop.run_forever()