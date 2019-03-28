#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 17:34
# @Author  : ChenYao
# @File    : coroutine_nest.py

'''loop.run_until_complete 使如何停止的？
    loop.run_until_complete 这个方法是如何做到运行完毕之后就停止的呢？
        看源码可以知道asyncio默认会给每一个task 调用add_done_callback 方法来添加一个回调函数_run_until_complete_cb
        这个方法可以使loop停止
'''

'''通过ctrl+c停止任务运行'''

import asyncio

async def get_html(slepp_times):
    print("waiting")
    await asyncio.sleep(slepp_times)
    print("done after {}s".format(slepp_times))


if __name__ == "__main__":
    task1 = get_html(2)
    task2 = get_html(1)
    task3 = get_html(3)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as ex:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
