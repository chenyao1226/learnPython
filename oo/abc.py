#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 20:41
# @Author  : ChenYao
# @File    : abc.py
'''抽象基本的应用场景1
    检查某个类是否有某个方法
'''


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


# 常规地我们想判断某个类是否有某个方法就可以使用hasattr方法
company = Company(["tom", "jerry"])
print(hasattr(company, "__len__"))

# 如果这个类有抽象基类的话就可以使用isintance方法
# collections.abc 模块下的Sized中的__len__方法是抽象基类（ @abstractmethod）方法，所以就可以用isinstance判断
from collections.abc import Sized

print(isinstance(company, Sized))

'''
collections.abc中有很多抽象基类
'''

'''抽象基类的应用场景2
    需要强制子类必须实现某些方法
'''


# 通过抛异常的方法实现强制子类实现某些方法
class CacheBase:
    def get(self):
        raise NotImplementedError

    def set(self):
        raise NotImplementedError


class RedisCache(CacheBase):
    pass


# redis_cache = RedisCache()
# redis_cache.get()   # 调用这个方法将会抛出异常
# redis_cache.set()   # 调用这个方法将会抛出异常

# 通过抽象基类的方法实现
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def set(self):
        pass


class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()
redis_cache.get()  # 调用这个方法将会抛出异常
redis_cache.set()  # 调用这个方法将会抛出异常

'''总结：
    不推荐使用抽象基类，最好通过其他的方法实现，不好理解。推荐使用鸭子类型
    推荐使用mixin做继承
'''
