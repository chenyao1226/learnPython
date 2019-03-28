#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 21:29
# @Author  : ChenYao
# @File    : select_http.py
import socket
from urllib.parse import urlparse

'''使用select实现http请求'''

import select
'''
pyhton中用select这个包，但是一般我们不使用这个包，而是使用selector，这个包是在select的基础上封装的，更加好用
并且会根据平台自动班我们选择使用select模型还是epoll模型
'''

from selectors import EVENT_WRITE, EVENT_READ, DefaultSelector

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 现在这一步讲不会阻塞
        except BlockingIOError as ex:
            pass

        selector.register(fileobj=self.client.fileno(), events=EVENT_WRITE, data=self.send)


    def send(self, key):
        selector.unregister(key.fd)  # 代码执行到这里说明已经监听到之前的定义的事件了，现在要把它取消掉
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, data=self.receive)

    def receive(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

        # 注册
        '''register有三个参数
            1. 文件描述符
            2. 监听事件
            3. 回调函数
        '''


def loop():
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == "__main__":
    f = Fetcher()
    f.get_url("http://www.baidu.com")
    loop()


'''
    利用select如何实现聊天群？
'''

'''回调之痛
    1. 可读性差
    2. 共享状态管理困难
    3. 异常处理困难
'''