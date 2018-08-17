# -*- coding: utf-8 -*-
import scrapy
from ShangHaiOne.items import ShanghaioneItem
import time
import re
import json
import hashlib
import time

class ZhejiangtwoSpider(scrapy.Spider):
    name = 'zhejiangtwo'
    #allowed_domains = ['www.zjjxw.gov.cn/col/col1108473/index.html?uid=3021488&pageNum=4']
    #start_urls = ['http://www.zjjxw.gov.cn/col/col1108473/index.html?uid=3021488&pageNum=4/']
    baseurl = "http://www.zjjxw.gov.cn/"
    startrecord = -44
    endrecord = 0
    perpage = 15
    columnid = "1108473"
    unitid = "3021488"
    url = 'http://www.zjjxw.gov.cn/module/jpage/dataproxy.jsp?'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",

    }


    def start_requests(self):


        # formdata = {
        #             "columnid":"1108473",
        #             "unitid":"3021488",
        #             }
        #
        # yield scrapy.FormRequest(
        #     url=url,
        #     headers=headers,
        #     formdata=formdata,
        #     callback=self.parse_page
        # )
        while self.endrecord < 271:
            self.startrecord += 45
            self.endrecord += 45
            self.perpage = 15
            formdata = {
                "columnid": "1108473",
                "unitid": "3021488",
            }
            formdata["startrecord"] = str(self.startrecord)
            formdata["endrecord"] = str(self.endrecord)
            formdata["perpage"] = str(self.perpage)

            yield scrapy.FormRequest(
                url=self.url,
                headers=self.headers,
                formdata=formdata,
                callback=self.parse_page
            )
            time.sleep(1)
    def parse_page(self, response):
        #list = response.xpath("//p/a/@href").extract()
        r = re.findall(r"art/.*?.html", response.body)
        for i in r:
            i = self.baseurl + i
        #print response.xpath("//a/@href").extract()
            yield scrapy.Request(i, callback=self.parse_one)
            # num = 2
            # if num<8:
            #     url = self.baseurl + str(num) + ".htm"
            #     yield scrapy.Request(url,callback=self.parse)
            #     num+=1

    def parse_one(self, response):
        item = ShanghaioneItem()
        item['title'] = response.xpath("//td[@class='title']/text()").extract()[0]
        title_link = response.xpath("//td[@class='title']/text()").extract()[0]

        m2 = hashlib.md5()
        m2.update(title_link.encode("utf-8"))
        item['md5'] = m2.hexdigest()
        times = response.xpath("//td[@style='line-height:20px;font-size:12px;']/text()").extract()[-1]
        try:
            time.strptime(times, "%Y-%m-%d")
            item['times'] = times
        except:
            item['times'] = ""
        item['content'] = response.xpath("//div[@id='zoom']").extract()
        item['yuan'] = "浙江省经济和信息化委员会"
        item["province"] = "浙江"
        yield item
