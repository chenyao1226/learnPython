#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 10:58
# @Author  : ChenYao
# @File    : test.py
from __future__ import absolute_import

from tornado.httpclient import HTTPClient

# 发起同步的http请求
def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.response


print(synchronous_fetch("http://www.baidu.com"))