#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 19:50
# @Author  : ChenYao
# @File    : select_test.py

import socket
from urllib.parse import urlparse

'''unix下五种IO模型
    阻塞式IO：
        遇IO就阻塞
    非阻塞式IO：
        1. 遇到IO立即返回，不会阻塞程序，节省时间
        2. 需要不断的询问内核IO操作有没有完成，这个过程会消耗cpu
        3. 如果IO操作完成了，就会把数据从内核空间复制到用户空间
    IO复用：
        select，poll，epoll
        1. IO复用其实也是阻塞式的，如果没有任何一个socket或者文件句柄准备好了，它也会阻塞
        2. 但是IO复用可以同时监听多个文件句柄，只要有文件句柄准备好了就会返回
        3. 文件句柄准备好了之后会把数据从内核空间复制到用户空间
    信号驱动式IO：
        操作系统准备好了之后，就会发一个信号给程序，这种模式用的很少
    异步IO：
        pass
'''
# 内核空间
# 用户空间
'''
select:
    1. 调用select之后会阻塞，直到有描述符就绪，或者超时
    2. 所有平台都支持select
    3. 单个进程能够监视的文件描述符最大为1024
    4. select通过遍历的方式找到就绪的描述符
poll：
    1. poll没有最大数量的限制
    2. 和select一样需要通过轮序的机制来获取就绪的描述符
epoll：
    1. 只在linux内核2.6之后的平台才支持
    2. 没有最大文件描述符限制
    3. 将用户关系的文件描述符存放到内核的一个时间列表中，这样在用户空间和内核空间的copy只需要一次
'''

'''epoll不一定比select好
    在高并发的情况下，连接活跃度不是很高，epoll比select好
    并发性不高，同时连接很活跃，select比epoll好
'''

'''=======================================我是分割线==================================='''

'''阻塞式IO编程'''


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))  # 这一步遇网络IO，会阻塞程序

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


'''非阻塞IO编程'''


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  # 这个设置可以把connect变成非阻塞的，connect会立即返回
    try:
        client.connect((host, 80))  # 现在这一步讲不会阻塞
    except BlockingIOError as ex:
        pass

    '''
        通过while循环的方式不断的尝试发送数据，因为socket连接可能会没有建立好连接，所以需要忽略异常
    '''
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as ex:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as ex:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    get_url("http://www.baidu.com")
