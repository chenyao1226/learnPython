#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 19:57
# @Author  : ChenYao
# @File    : first_test.py

# 事件循环+回调（驱动生成器）+epoll（IO多路复用）
# asyncio是python用于解决异步IO编程的一整套解决方案
# tornado，gevent，twisted（scrapy，django，channels）
# tornado（自己实现了web服务器），django+flask（uwsgi，gunicorn+nginx）
# torando可以直接部署，但是通常还是要配合nginx，nginx有更多的功能


import asyncio
import time

'''
在get_html方法中，我们想让程序sleep2s，可以使用time.sleep(2)，但是不推荐这么做，因为我们要进行的是高并发的编程
这种阻塞的代码不应该出现在协程中，asyncio.sleep(2)是是以协程的方式sleep了2s是非阻塞的, 如果使用了coroutine 就要使用await
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html("http://www.baidu.com"))
    print(time.time() - start_time)