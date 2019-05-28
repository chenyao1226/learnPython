#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 14:01
# @Author  : ChenYao
# @File    : use_iter.py

import requests

'''可迭代对象iterable
1. 如果一个对象是可迭代对象，使用python的内置函数iter()将会得到一个迭代器对象
2. 判断一个对象是不是可迭代，用collections模块中的Iterable进行isinstance判断
3. 如果一个对象是可迭代的，那么这对象所属的类一定实现了__iter__()方法或者__getitem__()
4. 可迭代对象不一定是迭代器对象，迭代器对象一定是可迭代对象
'''
l = [1,2,3]
s = {1, 2, 3}
t = (1, 2, 3)

'''迭代器对象iterator
1. 迭代器对象一定有一个next()方法, py2中是next(),py3中是__next__()
2. py的内置方法iter()可以将可迭代对象转化为迭代器对象，iter方法就是调用对象内置的__iter__方法
3. 调用__next__()方法的时候，如果超出了迭代范围将会抛出StopIteration异常
'''
l = [1, 2]
il = iter(l)
print(il.__next__())
print(il.__next__())
print(il.__next__())   # 这里将会抛出StopIteration异常

'''自己构造一个可迭代对象
第一步：构造一个迭代器对象，迭代器对象要继承collections的Iterator对象
第二步：使用这个迭代器对象构造可迭代对象，可迭代对象继承collections的Iterable对象
'''

from collections import Iterable, Iterator
# 迭代器对象，实现__next__方法
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city="+city)
        data = r.json()["data"]["forecast"][0]
        return "%s: %s. %s" %(city, data["low"], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

# 可迭代对象实现__iter__对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u"杭州", u"郑州"]):
    print(x)

'''使用生成器yield构造可迭代对象
需求：构造一个求出给定数值范围内多有素数的迭代器
'''

class PrimeNumbsers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 求素数
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2,k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrimeNum(k):
                yield k

'''反向迭代
需求：
    实现一个连续浮点数发送器，根据给定范围和步值产生一些列连续浮点数，如迭代FloatRange(3.0, 4.0, 0.2)
    正向：3.0->3.2->3.4->3.6->3.8->4.0
    反向：3.0->3.2->3.4->3.6->3.8->4.0
==========================================================
1. python有个和iter方法类似的内置函数reversed，但是reversed返回的是反向的迭代器
2. 对象的可迭代性是因为实现了__iter__方法，可以反向迭代就需要实现__reversed__方法
'''
l = [1, 2, 3]
# reversed方法可以实现反向迭代
for i in reversed(l):
    print(i)

class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end =end
        self.step = step

    def __iter__(self):
        t = self.start
        while t<= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

obj = FloatRange(1.0, 4.0, 0.5)

for i in iter(obj):
    print(i)

for i in reversed(obj):
    print(i)

'''对迭代器做切片操作
需求：
    我们想取到一个文件中两个指定行之间的内容，但是这个文件很大，不能将其全部读入到内存中
'''
from itertools import islice

f = open("use_iter.txt")  #  文件句柄是迭代器
lines = f.readlines()   # 这个方法将会将文件全部读取到内存中

f1 = islice(f, 2, 4)
for i in f1:
    print(i.strip())
# 从第一行取到第四行
f1 = islice(f, 4)
f.seek(0)   # 文件操作中有指针，要想重新开始需要seek
# 从第一行读取到最后一行
f2 = islice(f, 1, None)


'''如何在一个for循环中同时迭代多个对象
1. zip函数: 将多个迭代器中的元素组合成一个元素(元组)
2. itertools中的chain方法: 将多个迭代器按顺序合并成一个迭代器，类似于将两个列表相加
'''
# zip函数,长度不一致取较短的一个
for i in zip([1,2,3,4], ["a","b","c","d"]):
    print(i)

from itertools import chain
from random import randint

e1 = [randint(60, 100) for _  in range(40)]
e2 = [randint(60, 100) for _  in range(42)]
e3 = [randint(60, 100) for _  in range(43)]
e4 = [randint(60, 100) for _  in range(39)]

# 计算出大于90的元素有多少个
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 3:
        count +=1

