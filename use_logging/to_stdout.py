#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 16:42
# @Author  : ChenYao
# @File    : to_stdout.py

import logging

'''第一次使用logging
1. 没有设置日志输出到那个文件的话，默认输出到stdout
2. 默认输出的日志级别是warning，小于这个级别的话就不输出
'''

logging.basicConfig(level=logging.DEBUG)

logging.debug("haha")
logging.info("haha")
logging.warning("haha")
logging.error("haha")
logging.critical("haha")