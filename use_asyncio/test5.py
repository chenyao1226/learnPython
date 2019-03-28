#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:26
# @Author  : ChenYao
# @File    : test5.py

import asyncio
import time
from functools import partial

'''添加回调函数
    添加回调函数的话asyncio会自动给回调函数传递一个future类型的参数，所以callback方法应该至少有一个参数
    task.add_done_callback(send_mail) 只能添加回调函数，不会传递参数，那我们想要传递额外的参数应该怎么办呢？
        from functools import partial  可以把函数把包装成另外一个函数
        通过partial传递的参数应该放在future的前边
    
'''

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return True

# def send_mail(future):
#     print("send mail...")

def send_mail(name, future):
    print("send mail to {}".format(name))

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.baidu.com"))
    # task.add_done_callback(send_mail)
    task.add_done_callback(partial(send_mail, "chenyao"))
    loop.run_until_complete(task)
    print(time.time() - start_time)
    print(task.result())