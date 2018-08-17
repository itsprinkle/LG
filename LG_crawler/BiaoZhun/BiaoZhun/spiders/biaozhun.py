# -*- coding: utf-8 -*-
import hashlib
import scrapy
from BiaoZhun.items import BiaozhunItem
import time
from BiaoZhun.spiders.startURL import StartURL

class BiaozhunSpider(scrapy.Spider):
    name = 'biaozhun'
    baseurl = "http://www.csres.com"
    start_urls = StartURL.startURL

    #解析数据
    def parse(self,response):
        item = BiaozhunItem()
        if len(response.xpath("//td[@width='50%']/font/strong/text()")):
            item['bianhao'] = response.xpath("//td[@width='50%']/font/strong/text()").extract()[0]
        else:
            item['bianhao'] = ""
        if len(response.xpath("//tr/td/h3/text()")):
            item['nname'] = response.xpath("//tr/td/h3/text()").extract()[0]
        else:
            item['nname'] = ""


        # if len(response.xpath("//td/a/font/strong/text()")):
        #     item['bzzhuangtai'] = response.xpath("//td/a/font/strong/text()").extract()[0]
        # else:
        #     item['bzzhuangtai'] = "NULL"  //td/a/font/strong/strong/font/text()


        if len(response.xpath("//td/a/font/strong/strong/font/text()")):
            item['bzzhuangtai'] = response.xpath("//td/a/font/strong/strong/font/text()").extract()[0]
        else:
            item['bzzhuangtai'] = ""

        if len(response.xpath(u"//span/strong[text()='英文名称：']/../../../td[2]/span/text()")):
            item['enname'] = response.xpath(u"//span/strong[text()='英文名称：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['enname'] = ""


        if len(response.xpath(u"//span/strong[text()='中标分类：']/../../../td[2]/a/text()")):
            zh = response.xpath(u"//span/strong[text()='中标分类：']/../../../td[2]/a").xpath('string(.)').extract()
            item['classzh'] = "/".join(zh)
        else:
            item['classzh'] = ""


        if len(response.xpath(u"//span/strong[text()='ICS分类：']/../../../td[2]/a/text()")):
            sic = response.xpath(u"//span/strong[text()='ICS分类：']/../../../td[2]/a").xpath('string(.)').extract()
            item['classic'] = "/".join(sic)
        else:
            item['classic'] = ""


        if len(response.xpath(u"//span/strong[text()='发布部门：']/../../../td[2]/span/text()")):
            item['fbbumen'] = response.xpath(u"//span/strong[text()='发布部门：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['fbbumen'] = ""
        if len(response.xpath(u"//span/strong[text()='发布日期：']/../../../td[2]/span/text()")):
            item['fbriqi'] = response.xpath(u"//span/strong[text()='发布日期：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['fbriqi'] = ""
        if len(response.xpath(u"//span/strong[text()='实施日期：']/../../../td[2]/span/text()")):
            item['shishirq'] = response.xpath(u"//span/strong[text()='实施日期：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['shishirq'] = ""
        if len(response.xpath(u"//span/strong[text()='提出单位：']/../../../td[2]/span/text()")):
            item['tichudw'] = response.xpath(u"//span/strong[text()='提出单位：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['tichudw'] = ""
        if len(response.xpath(u"//span/strong[text()='归口单位：']/../../../td[2]/span/text()")):
            item['guikoudw'] = response.xpath(u"//span/strong[text()='归口单位：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['guikoudw'] = ""
        if len(response.xpath(u"//span/strong[text()='主管部门：']/../../../td[2]/span/text()")):
            item['zhuguanbm'] = response.xpath(u"//span/strong[text()='主管部门：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['zhuguanbm'] = ""
        if len(response.xpath(u"//span/strong[text()='起草单位：']/../../../td[2]/span/text()")):
            item['qicaodw'] = response.xpath(u"//span/strong[text()='起草单位：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['qicaodw'] = ""
        if len(response.xpath(u"//span/strong[text()='起草人：']/../../../td[2]/span/text()")):
            item['qicaoren'] = response.xpath(u"//span/strong[text()='起草人：']/../../../td[2]/span/text()").extract()[0]
        else:
            item['qicaoren'] = ""
        if len(response.xpath(u"//span/strong[text()='替代情况：']/../../../td[2]/span|a/text()")):
            item['tidaiqingkuang'] = \
            response.xpath(u"//span/strong[text()='替代情况：']/../../../td[2]/span|a/text()").extract()[0]
        else:
            item['tidaiqingkuang'] = ""
        if len(response.xpath(u"//td[text()='标准简介']/../../../..")):
            item['bajianjie'] = response.xpath(u"//td[text()='标准简介']/../../../..").extract()
        else:
            item['bajianjie'] = ""

        yield item
