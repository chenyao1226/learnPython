import requests
from collections.abc import Iterator, Iterable

'''可迭代对象和迭代器
    1. 可迭代对象：实现了__iter__或者__getitem__方法的对象
    2. 迭代器对象：实现了__next__方法的对象
    3. 可迭代对象不一定是迭代器对象，迭代器对象一定是可迭代对象，因为Iterable是iterator的基类
    4. 将一个可迭代对象作为参数传递给iter()方法将会得到一个迭代器对象
'''

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


w = WeatherIterator(["吉林", "长春", "郑州"])

'''自己实现可迭代对象
    1. 先构造一个迭代器，然后实现可迭代对象的__iter__方法
    2. 通过生成器yield实现__iter__方法
'''


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

'''通过生成器yield实现可迭代对象'''
class Company:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __iter__(self):
        for item in self.employee_list:
            yield item

if __name__ == "__main__":
    com = Company(["eric", "tom", "jerry"])
    for item in com:
        print(item)