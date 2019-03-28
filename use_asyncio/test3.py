#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:15
# @Author  : ChenYao
# @File    : test3.py

import asyncio
import time

'''拿到任务的返回值
    运行任务前先用asyncio.ensure_future方法对任务进行包装一下(会返回一个future类，这个类和多线程中的future很类似)
    然后再运行，执行完毕之后就可以通过result方法拿到返回值
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future_task = asyncio.ensure_future(get_html("http://www.baidu.com"))
    loop.run_until_complete(future_task)
    print(time.time() - start_time)
    print(future_task.result())