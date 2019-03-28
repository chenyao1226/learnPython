#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 19:50
# @Author  : ChenYao
# @File    : use_fileconfig.py
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("example01")
# logger = logging.getLogger()

logger.info("hahaha")

