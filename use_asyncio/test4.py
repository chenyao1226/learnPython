#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:20
# @Author  : ChenYao
# @File    : test4.py

import asyncio
import time

'''拿到任务的返回值
    用loop的create_task方法创建任务，再拿去执行，就可以获取到返回值
    它和asyncio.ensure_future方法的道理是一样的，查看ensure_future方法源码就可以看到这个方法会先执行loop = events.get_event_loop()
    拿到loop之后，再调用create_task方法
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.baidu.com"))
    loop.run_until_complete(task)
    print(time.time() - start_time)
    print(task.result())