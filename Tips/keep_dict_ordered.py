#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 1:20
# @Author  : ChenYao
# @File    : keep_dict_ordered.py

from collections import OrderedDict

'''
让字典保持有序,是字典能够像列表那样能按照元素进入的顺序排列
'''

d = OrderedDict()
d["jim"] = (1, 35)
d["Tom"] = (2, 36)
d["Bob"] = (3, 40)

for x in d:
    print(x)


