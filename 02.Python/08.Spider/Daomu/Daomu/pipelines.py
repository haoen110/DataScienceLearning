# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入settings模块，可使用定义的相关变量
from Daomu import settings
import pymongo
import pymysql

class DaomuPipeline(object):
    def process_item(self, item, spider):
        print("==================")
        # 书名
        print(item["book"])
        # 标题
        print(item["title"])
        # 章节名称
        print(item["chapter"])
        # 章节数
        print(item["chapter_num"])
        # 章节链接
        print(item["chapter_url"])
        print("==================")

class MongoPipeline(object):
    def __init__(self):
        host = "127.0.0.1"
        port = 27017

        conn = pymongo.MongoClient(host=host, port=port)
        db = conn.spiderdb
        self.myset = db.daomubiji

    def process_item(self, item, spider):
        # 把item对象转为字典
        book_info = dict(item)
        self.myset.insert(book_info)
        print("存入数据库成功")


class MysqlPipeline:
    def __init__(self):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        pwd = settings.MYSQL_PWD
        dbname = settings.MYSQL_DB
        self.db = pymysql.connect(host=host, user=user, password=pwd, db=dbname)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into daomubiji values(%s, %s, %s, %s, %s)'
        L = [item['book'], item['title'], item['chapter'], item['chapter_num'], item['chapter_url']]
        self.cursor.execute(ins, L)
        self.db.commit()




