#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 14:09
# @Author  : ChenYao
# @File    : thread_queue_test.py
#通过queue的方式进行线程间同步

from queue import Queue


import time
import threading


def get_detail_html(queue):
    #爬取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")
        queue.task_done()


def get_detail_url(queue):
    # 爬取文章列表页
    # while True:
        print("get detail url started")
        # time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


#1. 线程通信方式- 共享变量

if  __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)


    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()
    detail_url_queue.join()

    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))

'''
queue对象的task_done和join方法：
    join方法会阻塞程序，只有当queue为空的时候才会继续向下执行，否则就会一直处于挂起的状态
    task_done应该应用于get方法之后，告诉queue我刚刚取出来的这个任务已经完成了，
    
    如果使用了jion方法那么在完成一个任务之后必须调用join方法，否则即使任务已经被全部完成了，join方法还是阻塞程序
'''

'''
线程间通信还有一种方式就是通过共享变量，通过声明global和Lock的使用完成线程间通信
'''