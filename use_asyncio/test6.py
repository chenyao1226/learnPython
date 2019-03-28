#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:35
# @Author  : ChenYao
# @File    : test6.py


import asyncio
import time

'''gather也用来一次性提交多个任务
    1. 将任务分组
    2. 取消任务


    直接提交任务的话需要用*
    先gather则不用*
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks1 = [get_html("http://www.baidu.com") for i in range(10)]
    tasks2 = [get_html("http://www.jd.com") for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks1, *tasks2))  # 加*可以直接提交任务
    tasks1 = asyncio.gather(*tasks1)
    tasks2 = asyncio.gather(*tasks2)
    # 取消任务
    # tasks1.cancel()
    loop.run_until_complete(asyncio.gather(tasks1, tasks2))
    print(time.time() - start_time)