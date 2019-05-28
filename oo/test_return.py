#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 20:57
# @Author  : ChenYao
# @File    : test_return.py

def exe_try():
    try:
        print("code started.")
        raise KeyError
        return 1
    except KeyError as ex:
        print("key error")
        return 2
    else:
        print("key error")
        return 3
    finally:
        print("finally")
        return 4


if __name__ == "__main__":
    result = exe_try()
    print(result)

'''
当return语句和except一起使用的时候，具体会在哪里执行return呢？  只需要记住：如果会有多个地方return，那么将会执行压栈的操作
当所有的代码执行完了之后，从栈顶取出一个return值作为返回值
'''
