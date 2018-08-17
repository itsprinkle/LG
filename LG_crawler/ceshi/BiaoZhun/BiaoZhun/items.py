# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiaozhunItem(scrapy.Item):
    # define the fields for your item here like:
    nname = scrapy.Field()
    bianhao = scrapy.Field()
    bzzhuangtai = scrapy.Field()
    enname = scrapy.Field()
    classzh = scrapy.Field()
    classic = scrapy.Field()
    fbbumen = scrapy.Field()
    fbriqi = scrapy.Field()
    shishirq = scrapy.Field()
    tichudw = scrapy.Field()
    guikoudw = scrapy.Field()
    zhuguanbm = scrapy.Field()
    qicaodw = scrapy.Field()
    qicaoren = scrapy.Field()
    tidaiqingkuang = scrapy.Field()
    bajianjie = scrapy.Field()
