#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 10:21
# @Author  : ChenYao
# @File    : first_demo.py
import use_tornado.ioloop
import use_tornado.web

class MainHandler(use_tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world!")

application = use_tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    use_tornado.ioloop.IOLoop.instance().start()
