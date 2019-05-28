#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:02
# @Author  : ChenYao
# @File    : gen_advanced.py

'''send方法
    1. yield 方法可以返回一个值，同时也可以在外部往里传递一个值，就是yield是提供了一个通道，既可以向里传，也可以向外传
    2. 在生成器没有启动的情况下，即：这个生成器还没有调用过next方法也没有调用过send方法，
        这时候如果向生成器send一个非None数据的话是会报错的
    3. yield的send方法会消耗一次生成器
'''


def gen_func():
    v1 = yield 1
    print("1:", v1)
    v2 = yield 2
    print("2:", v1)
    v3 = yield 3
    print("3:", v1)
    v4 = yield 4
    print("4:", v1)
    return "haha"


gen = gen_func()
gen.send(None)  # 第一次执行生成器采用了send方法，这里已经消耗了一次生成器,我们已经取不到 http://www.baidu.com了
print(next(gen))
gen.send(1)
print(next(gen))
# gen.send(2)
print(next(gen))
# gen.send()

'''close方法
    1. 执行完close方法之后，如果继续调用生成器是会报错的
'''


def gen_func():
    yield "http://www.baidu.com"
    yield 2
    yield 3
    yield 4


# gen = gen_func()
# print(next(gen))
# gen.close()
# print(gen.send(None))
# print(next(gen))


'''throw
    1. 在外部调用生成器的throw方法可以向生成器里边抛异常
    2. throw方法也会像next和send方法一样会消耗一次生成器
    3. throw把异常抛给的是上一次的yield
    
'''


def gen_func():
    try:
        yield 1
    except Exception:
        print("第1个yield")
    try:
        yield 2
    except Exception:
        print("第2个yield")
    try:
        yield 3
    except Exception:
        print("第3个yield")
    try:
        yield 4
    except Exception:
        print("第4个yield")
    yield 5

# gen = gen_func()
# print(next(gen))
# gen.throw(Exception, "err1")
# print(next(gen))
# gen.throw(Exception, "err2")
# print(next(gen))
