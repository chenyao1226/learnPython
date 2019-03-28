#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 17:50
# @Author  : ChenYao
# @File    : use_logger.py
import logging

'''Logger
1. logger是记录器，要想记录日志必须先创建logger
2. 没有显式创建的话就会创建一个默认的rootlogger,并应用默认的日志级别warning
3. 创建方式：logger = logging.getLogger(logger_name)
4. 获取到Logger之后，可以调用setLevel设置日志的记录级别
'''

logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

'''Handler
1. 处理器将记录的日志发送到合适地方
2. 常见的Handler：StreamHandler，FileHandler，NullHandler
3. 创建方法：
    StreamHandler：
        sh = logging.StreamHandler(stream=None)
    FileHandler：
        fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
    NullHandler
        不做任何格式的输出
'''
log_path = "./test.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

'''Formatter
1. 格式化器，设置日志信息的规则，结构和内容
2. 默认的时间格式为：%Y-%m-%d %H:%M:%S
3. 创建方法：formatter = logging.Formatter(fmt=None, datefmt=None)
'''
fmt = "%(asctime)-15s~%(levelname)s~%(filename)s~%(lineno)d~%(process)d~%(message)s"
tfmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, tfmt)

'''Filter（用的比较少）
1. 过滤器，实现更加复杂的过滤
'''

'''将logger, handler, formatter组合起来
'''
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

# ================================================我是分割线================================================
'''日志的配置方式
1. basicConfig()    # 简单方式配置
1. fileConfig()     # 通过配置文件
1. dictConfig()     # 通过配置字典
1. listen()         # 进行网络配置
'''