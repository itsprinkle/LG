# -*- coding: utf-8 -*-
import scrapy
from ShangHaiOne.items import ShanghaioneItem
import hashlib
import time

class JiangsuSpider(scrapy.Spider):
    name = 'jiangsu'
    allowed_domains = ['www.jseic.gov.cn']
    start_urls = ['http://www.jseic.gov.cn/xwzx/zcfb/bwzc/']
    baseurl = "http://www.jseic.gov.cn/xwzx/zcfb/bwzc/index_"
    num = 2
    urlone = "http://www.jseic.gov.cn/xwzx/zcfb/bwzc"

    def parse(self, response):

        list = response.xpath("//li[@class='ft14lh30']//a/@href").extract()
        for i in list:
            i = i[1:]
            i = self.urlone + i
            print i
            yield scrapy.Request(i, callback=self.parse_one)
            #num = 1的时候,是第二页

        if self.num<41:
            url = self.baseurl + str(self.num) + ".html"
            yield scrapy.Request(url,callback=self.parse)
            self.num+=1

    def parse_one(self, response):
        item = ShanghaioneItem()
        item['title'] = response.xpath("//div[@class='nstit']/h1/text()").extract()[0]
        title_link = response.xpath("//div[@class='nstit']/h1/text()").extract()[0]

        m2 = hashlib.md5()
        m2.update(title_link.encode("utf-8"))
        item['md5'] = m2.hexdigest()
        times = response.xpath("//div[@class='nstimes0']/text()").extract()[0].strip().split()[2][3:]
        try:
            time.strptime(times, "%Y-%m-%d")
            item['times'] = times
        except:
            item['times'] = ""
        item['content'] = response.xpath("//div[@class='TRS_Editor']").extract()[0]
        item['yuan'] = "江苏省经济和信息化委员会"
        item["province"] = "江苏"
        yield item
