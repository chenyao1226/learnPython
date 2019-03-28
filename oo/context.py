#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 21:18
# @Author  : ChenYao
# @File    : context.py
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield
    print("file close")


with file_open("demo.txt") as fb:
    print("file processing...")