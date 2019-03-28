#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:08
# @Author  : ChenYao
# @File    : test2.py

import asyncio
import time

'''一次性提交多个任务
    asyncio.wait()会等待所有的协程都执行完毕之后才会继续向下执行
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
