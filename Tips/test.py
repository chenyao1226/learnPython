#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 22:52
# @Author  : ChenYao
# @File    : del_useless_str.py

import mmap
with open("demo.txt", 'wt') as fb:
    fb.write("你好吗")


with open("demo.txt", 'r+t') as fb:
    # 三个参数依次是文件描述符，映射的文件大小（0是全映射），访问权限
    m = mmap.mmap(fileno=fb.fileno(), length=0,access=mmap.ACCESS_WRITE)
    print(len(m))