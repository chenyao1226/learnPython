#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 22:59
# @Author  : ChenYao
# @File    : use_orm.py
import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("mysql://root:meidi@192.168.163.83/news?charset=utf8")
Base = declarative_base()

Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = "news_test"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300),)
    author = Column(String(200),)
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)

'''创建表'''
# News.metadata.create_all(engine)

class OrmTest:
    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(
            title="标题1",
            content="内容1",
            types="类型1",
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据
            默认查询主键
         '''
        return self.session.query(News).get(1)

    def get_all(self):
        return self.session.query(News).filter_by(is_valid=1)

    def update_data(self):
        obj = self.session.query(News).get(38)
        obj.is_valid = 0
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete_data(self):
        data = self.session.query(News).get(39)
        self.session.delete(data)
        self.session.commit()

if __name__ == "__main__":
    obj = OrmTest()
    ret = obj.add_one()
    print(ret.id)
