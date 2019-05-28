#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 22:52
# @Author  : ChenYao
# @File    : del_useless_str.py
'''去掉不需要的字符串
需求：
    1. 过滤掉用户输入中前后多余的空白字符
    2. 过滤某windows下编辑文本中的\r, 'hello world\r\n'
    3. 去掉文本中的unicode组合符号(音调)
'''

# 方法一
s = "   abc  123   123   "
s.strip()
s.lstrip()
s.rstrip()

s = "----abc+++++"
s.strip("+-")

# 方法二  删除固定位置下的字符
s = 'abc:123'
# print(s[:3] + s[4:])

# 方法三 replace或者re.sub
import re
import string
s = '\tabc\t123\rtxyz'
s.replace("\t", "")
re.sub('[\t\r]', '', s)

# translate方法
s = 'abc\rrefg\n2342\t'
table = ''.maketrans({'\r':None, '\t':None, '\n':None})
print(s.translate(table))
