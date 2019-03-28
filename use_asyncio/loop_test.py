#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 14:33
# @Author  : ChenYao
# @File    : loop_test.py

# 事件循环+回调（驱动生成器）+epoll（IO多路复用）
# asyncio是python用于解决异步IO编程的一整套解决方案
# tornado，gevent，twisted（scrapy，django，channels）
# tornado（自己实现了web服务器），django+flask（uwsgi，gunicorn+nginx）
# torando可以直接部署，但是通常还是要配合nginx，nginx有更多的功能

import asyncio
import time
from functools import partial

async def get_heml(url):
    print("start get url")
    # 不能使用time.sleep()方法，因为这个方法是阻塞的
    # await方法后面跟的应该是一个协程对象
    await asyncio.sleep(2)
    print("end get url")
    return True


# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     '''
#     提交单个任务
#     '''
#     #loop.run_until_complete(get_heml("http://www.baidu.com"))
#     '''
#     提交多个任务
#     '''
#     tasks = [get_heml("http://www.baidu.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     '''
#     gather方法调用多个方法
#     gather比wait更加high-level
#     '''
    # group1 = [get_heml("http://www.baidu.com") for i in range(2)]
    # group2 = [get_heml("http://www.baidu.com") for i in range(2)]
    # group1 = asyncio.gather(*group1)
    # group2 = asyncio.gather(*group2)
    # group1.cancel()
    # group2.cancel()
#     loop.run_until_complete(asyncio.gather(*group1, *group2))

#     end_time = time.time()
#     print(end_time - start_time)


'''
获取协程的返回值
'''

async def get_html(url):
    print("start get url")
    # 不能使用time.sleep()方法，因为这个方法是阻塞的
    # await方法后面跟的应该是一个协程对象
    await asyncio.sleep(2)
    print("end get url")
    return True


def callback(url, future):
    print("send email to cy")
    if url:
        print(url)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 方式1
    # get_future = asyncio.ensure_future(get_heml("http://www.baidu.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 方式2
    task = loop.create_task(get_html("http://www.baidu.com"))
    # 还可以添加回调函数，回调函数至少应该有一个参数，因为会给回调函数传递一个future
    # task.add_done_callback(callback)
    # 对回调函数进行二次包装
    task.add_done_callback(partial(callback, "http://www.baidu.com"))
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start_time)
