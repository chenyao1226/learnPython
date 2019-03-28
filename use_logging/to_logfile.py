#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 16:45
# @Author  : ChenYao
# @File    : to_logfile.py
import logging

logging.basicConfig(filename="to_logfile.log", level=logging.DEBUG)

logging.debug("haha")
logging.info("haha")
logging.warning("haha")
logging.error("haha")
logging.critical("haha")