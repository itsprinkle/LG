# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
from scrapy import signals
import json
import codecs
import re
import time
from scrapy import log
import time
import MySQLdb
import hashlib

class ShanghaionePipeline(object):

    def __init__(self):
        self.f = open("123.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()

class MySQLPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host = "192.168.1.207",
                                            port = 3308,
                                            db = "policy",            # 数据库名
                                            user = "yangchaoming",       # 数据库用户名
                                            passwd = "ycm@2017",     # 密码
                                            cursorclass = MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=True

                                            )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):

        tb.execute("insert ignore into policy (title,time,content,yuan,province,md5) values (%s,%s,%s,%s,%s,%s)",(item["title"], item["times"], item["content"],item["yuan"],item["province"],item["md5"]))
        log.msg("Item data in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
