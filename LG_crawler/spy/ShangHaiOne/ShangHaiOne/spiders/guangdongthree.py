# -*- coding: utf-8 -*-
import scrapy
from ShangHaiOne.items import ShanghaioneItem
import re
import hashlib
import time

class GuangdongthreeSpider(scrapy.Spider):
    name = 'guangdongthree'
    allowed_domains = ['www.gdei.gov.cn']
    start_urls = ['http://www.gdei.gov.cn/ywfl/jsgz/']
    baseurl = "http://www.gdei.gov.cn/ywfl/jsgz/index_"
    num = 1
    def parse(self, response):
        # list = response.xpath("//li[@class='ft14lh30']//a/@href").extract()
        r = re.findall(r"/\d+.*\.htm", response.body)
        for i in r:
            # print i
            yield scrapy.Request("http://www.gdei.gov.cn/ywfl/jsgz" + i, callback=self.parse_one)
            # num = 1的时候,是第二页,10ye

            if self.num<10:
                url = self.baseurl + str(self.num) + ".htm"
                yield scrapy.Request(url,callback=self.parse)
                self.num+=1

    def parse_one(self, response):
        item = ShanghaioneItem()
        item['title'] = re.findall(r'<h1>.*?</h1>', response.body)[0].decode("gbk")[4:-5]
        title_link = re.findall(r'<h1>.*?</h1>', response.body)[0].decode("gbk")[4:-5]

        m2 = hashlib.md5()
        m2.update(title_link.encode("utf-8"))
        item['md5'] = m2.hexdigest()
        times = re.findall(r"t =\'.*\'", response.body)[0][4:-1]
        try:
            time.strptime(times, "%Y-%m-%d")
            item['times'] = times
        except:
            item['times'] = ""
        #item['content'] = response.xpath("//div[@id='zoom']/div").extract()[0]
        if response.xpath("//div[@id='zoom']/div"):
            item['content'] = response.xpath("//div[@id='zoom']/div").extract()[0]
        else:
            item['content'] = ""
        item['yuan'] = "广东省经济和信息化委员会"
        item["province"] = "广东"
        # print item
        yield item

