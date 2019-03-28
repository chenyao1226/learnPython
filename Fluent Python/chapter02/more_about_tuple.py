#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 10:29
# @Author  : ChenYao
# @File    : more_about_tuple.py
from collections import namedtuple

lax_coordinates = (33.9425, -118.408056)

'''元组拆包'''
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in traveler_ids:
    print("%s/%s" % passport)
for country, _ in traveler_ids:
    print(country)

'''
    * 运算符可以把一个可迭代对象拆开作为函数的参数
'''
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)

'''
用*处理剩下的元素,函数用*args来获取不确定数量的参数算是一种经典的写法了
在平行赋值中，* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的
任意位置
'''
a, b, *rest = range(5)
print(rest)
a, *body, c, d = range(5)
*head, b, c, d = range(5)

'''
嵌套元组拆包
'''
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

'''
具名元组
    创建一个具名元组需要两个参数，一个是类名，一个是各个字段的名字
        后者可以是由各个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
        
    具名元组的_asdict()方法可以将元组以collections.OrderedDict的形式返回
'''
# City = namedtuple('City', 'name country population coordinates')
City = namedtuple('City', ['name','country','population' ,'coordinates'])
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)
print(City._fields)
print(tokyo._asdict())