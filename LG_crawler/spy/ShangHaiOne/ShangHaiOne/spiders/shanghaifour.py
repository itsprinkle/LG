# -*- coding: utf-8 -*-
import scrapy
from ShangHaiOne.items import ShanghaioneItem
import sys
import hashlib
import time
reload(sys)
sys.setdefaultencoding("utf-8")
import re

class ShanghaifourSpider(scrapy.Spider):
    name = 'shanghaifour'
    allowed_domains = ['www.sheitc.gov.cn/cyfz/index_1.htm']
    start_urls = ['http://www.sheitc.gov.cn/cyfz/index_1.htm']
    baseurl = "http://www.sheitc.gov.cn/cyfz/index_"
    num = 2

    def parse(self, response):
        #list = response.xpath("//p/a/@href").extract()
        r = re.findall(r"http.*cyfz.*?htm", response.body)
        for i in r:
            print i
            yield scrapy.Request(i, callback=self.parse_one)

        if self.num<33:
            url = self.baseurl + str(self.num) + ".htm"
            yield scrapy.Request(url,callback=self.parse)
            self.num+=1

    def parse_one(self, response):
        item = ShanghaioneItem()
        item['title'] = response.xpath("//h1[@id='ivs_title']/text()").extract()[0]
        title_link = response.xpath("//h1[@id='ivs_title']/text()").extract()[0]

        m2 = hashlib.md5()
        m2.update(title_link.encode("utf-8"))
        item['md5'] = m2.hexdigest()
        a = response.xpath("//h3[@class='view_tit_1']/text()").extract()[0]
        times = re.findall(r"\d.*\d", a)[0]
        try:
            time.strptime(times, "%Y-%m-%d")
            item['times'] = times
        except:
            item['times'] = ""
        item['content'] = response.xpath("//div[@id='ivs_content']").extract()[0]
        item['yuan'] = "上海市经济和信息化委员会"
        item["province"] = "上海"
        yield item

