#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 10:01
# @Author  : ChenYao
# @File    : file_op.py

'''IO高效处理
1. py2写入文件前对unicode编码，读入文件后对二进制字符串解码
    如果将要写入的内容是unicode编码的，默认就会先编码为utf8再写入文件，读取该内容的时候默认也是先会解码
2. py3 open函数指定‘t’的文本模式，encoding指定编码格式
'''

'''
py2中文本操作的过程，我们可以指定encode和decode类型，也可以不指定，不指定的时候默认会采用utf8进行编解码
注意：这段代码在py2中运行才可以，py3中运行会报错
'''

s = u'你好'
with open('py2.txt', 'w') as f:
    f.write(s.encode("gbk"))

with open('py2.txt', 'r') as f:
    c = f.read()

print(c.decode("gbk"))


'''
py3中文本的操作
'''
s = "你好"
with open("py3.txt", 'wt', encoding='utf-8') as f:
    f.write(s)

with open("py3.txt", 'rt', encoding='utf-8') as f:
    c = f.read()
print(c)


'''设置文件缓冲
    为了减少IO的次数，我们可以设置文件缓冲
    
    1. 全缓冲（buffering设置成1024*n）
        f = open("demo.tx", "wt", encoding="utf8", buffering=4096)
    2. 行缓冲
            f = open("demo.tx", "wt", encoding="utf8", buffering=1)
    3. 无缓冲
            f = open("demo.tx", "wt", encoding="utf8", buffering=0)
'''

'''将文件映射到内存
    想要把文件映射到内存需要拿到这个文件的文件描述符
'''
import mmap
with open("demo.txt", 'r+') as fb:
    # 三个参数依次是文件描述符，映射的文件大小（0是全映射），访问权限
    m = mmap.mmap(fileno=fb.fileno(), length=0,access=mmap.ACCESS_WRITE)


'''使用临时文件
    关闭文件之后就删除
'''
from tempfile import TemporaryFile, NamedTemporaryFile
# 系统是找不到这个文件的， 只能有单进程访问
f = TemporaryFile()
f.write("abcd" * 10000)
f.seek(0)
f.read(100)

# 可以由多个进程访问
ntf = NamedTemporaryFile()
