#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 22:14
# @Author  : ChenYao
# @File    : test_mysql.py

import MySQLdb


class MysqlSearch:
    def __init__(self):
        self.host = "192.168.163.83"
        self.port = 3306
        self.user = "root"
        self.pwd = "meidi"
        self.db = "news"

        self.conn = None
    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                passwd = self.pwd,
                db=self.db,
                charset ="utf8")
        except MySQLdb.Error as ex:
            print(ex)

    def get_one(self):
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `id` DESC;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ("国际",))
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        cursor.close()
        return rest

    def get_all(self):
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `id` DESC;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('国际', ))
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        print(rest)
        cursor.close()

    def get_more_by_page(self, page, page_size):
        offset = (page - 1) * page_size
        sql = "SELECT * FROM `news` WHERE `types` = '%s' ORDER BY `id` DESC LIMIT %s %s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ("国际", offset, page_size))
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall]
        cursor.close()
        return rest

    def add_one(self):
        try:
            sql = ('INSERT INTO `news`(`title`,`image`,`content`,`author`,`types`) '
                   'VALUE (%s, %s, %s, %s, %s);')
            cursor = self.conn.cursor()
            cursor.execute(sql, ("标题1", "/static/img/news/01.jpg", "内容1", "chenyao", "推荐"))
            self.conn.commit()
            cursor.close()
        except MySQLdb.Error as ex:
            print(ex)
            self.conn.rollbakc()

    def close(self):
        self.conn.close()



if __name__ == "__main__":
    obj = MysqlSearch()
    obj.get_conn()
    # obj.get_one()
    # obj.get_all()
    obj.add_one()
    obj.close()