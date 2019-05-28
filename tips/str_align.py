#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 22:44
# @Author  : ChenYao
# @File    : str_align.py

s = "abc"
#=========================方法一================================
s.ljust(20)
s.ljust(20, "=")

s.rjust(20)
s.rjust(20, "=")

s.center(20)
s.center(20, "=")
#=====================方法二====================================

format(s, "<20")
print(format(s, ">20"))
format(s, "^20")