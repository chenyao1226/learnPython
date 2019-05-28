#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0:18
# @Author  : ChenYao
# @File    : UseXml.py

from xml.etree.ElementTree import parse

'''
根节点
一个元素可以有多个属性
有个元素可以有多个文本
'''

# 解析xml文件
f = open("demo.xml")
et = parse(f)

et.get()
# 获取根节点
root = et.getroot()

root.tag
root.attr
root.text

for child in root:
    print child.get('name')

root.find("country")  #返回第一个找到的元素
root.findall("country")
root.findall("country[1]")
root.findall("country[last()]")
root.findall("country[last()-1]")
root.iterfind("country")
for e in root.iterfind("country"):
    print e.get("name")

root.findall("country/*") # 查找所有的孙子节点
root.findall("./rank/..")
root.findall("country[@name]")
root.findall("country[@name='china']")

root.findall("country[rank]")
root.findall("country[rank='test']")

# iter可以查找所有的子节点
root.iter()



'''
构建一个xml
'''

from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import tostring
e = Element("Data")
e.tag
e.set("name", 'abc')

tostring(e)
e.text = '123'
tostring(e)

e2 = Element("Row")
e3 = Element("Open")
e3.text = '8.80'
e2.append(e3)
tostring(e2)
e.append(e2)
tostring(e)

et = ElementTree(e)
et.write("demo.xml")
