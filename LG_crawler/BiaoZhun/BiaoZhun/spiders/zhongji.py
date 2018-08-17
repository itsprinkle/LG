# -*- coding: utf-8 -*-
import hashlib
import scrapy
from BiaoZhun.items import BiaozhunItem
import time
import random
#from BiaoZhun.spiders.startURL import StartURL

class BiaozhunSpider(scrapy.Spider):
    name = 'zhongji'
    #allowed_domains = ['www.csres.com']
    urls = ['http://www.csres.com/sort/chsortdetail/A.html#A00/09',
'http://www.csres.com/sort/chsortdetail/A.html#A10/19',
'http://www.csres.com/sort/chsortdetail/A.html#A20/39',
'http://www.csres.com/sort/chsortdetail/A.html#A40/49',
'http://www.csres.com/sort/chsortdetail/A.html#A50/64',
'http://www.csres.com/sort/chsortdetail/A.html#A65/74',
'http://www.csres.com/sort/chsortdetail/A.html#A75/79',
'http://www.csres.com/sort/chsortdetail/A.html#A80/89',
'http://www.csres.com/sort/chsortdetail/A.html#A90/94',
'http://www.csres.com/sort/chsortdetail/B.html#B00/09',
'http://www.csres.com/sort/chsortdetail/B.html#B10/14',
'http://www.csres.com/sort/chsortdetail/B.html#B15/19',
'http://www.csres.com/sort/chsortdetail/B.html#B20/29',
'http://www.csres.com/sort/chsortdetail/B.html#B30/39',
'http://www.csres.com/sort/chsortdetail/B.html#B40/49',
'http://www.csres.com/sort/chsortdetail/B.html#B50/59',
'http://www.csres.com/sort/chsortdetail/B.html#B60/79',
'http://www.csres.com/sort/chsortdetail/B.html#B90/99',
'http://www.csres.com/sort/chsortdetail/C.html#C00/09',
'http://www.csres.com/sort/chsortdetail/C.html#C10/29',
'http://www.csres.com/sort/chsortdetail/C.html#C30/49',
'http://www.csres.com/sort/chsortdetail/C.html#C50/64',
'http://www.csres.com/sort/chsortdetail/C.html#C65/74',
'http://www.csres.com/sort/chsortdetail/C.html#C75/79',
'http://www.csres.com/sort/chsortdetail/C.html#C80/89',
'http://www.csres.com/sort/chsortdetail/C.html#C90/99',
'http://www.csres.com/sort/chsortdetail/D.html#D00/09',
'http://www.csres.com/sort/chsortdetail/D.html#D10/19',
'http://www.csres.com/sort/chsortdetail/D.html#D20/29',
'http://www.csres.com/sort/chsortdetail/D.html#D30/39',
'http://www.csres.com/sort/chsortdetail/D.html#D40/49',
'http://www.csres.com/sort/chsortdetail/D.html#D50/59',
'http://www.csres.com/sort/chsortdetail/D.html#D80/89',
'http://www.csres.com/sort/chsortdetail/D.html#D90/99',
'http://www.csres.com/sort/chsortdetail/E.html#E00/09',
'http://www.csres.com/sort/chsortdetail/E.html#E10/19',
'http://www.csres.com/sort/chsortdetail/E.html#E20/29',
'http://www.csres.com/sort/chsortdetail/E.html#E30/49',
'http://www.csres.com/sort/chsortdetail/E.html#E60/69',
'http://www.csres.com/sort/chsortdetail/E.html#E90/99',
'http://www.csres.com/sort/chsortdetail/F.html#F00/09',
'http://www.csres.com/sort/chsortdetail/F.html#F10/19',
'http://www.csres.com/sort/chsortdetail/F.html#F20/29',
'http://www.csres.com/sort/chsortdetail/F.html#F40/49',
'http://www.csres.com/sort/chsortdetail/F.html#F50/59',
'http://www.csres.com/sort/chsortdetail/F.html#F60/69',
'http://www.csres.com/sort/chsortdetail/F.html#F70/79',
'http://www.csres.com/sort/chsortdetail/F.html#F80/89',
'http://www.csres.com/sort/chsortdetail/F.html#F90/99',
'http://www.csres.com/sort/chsortdetail/G.html#G00/09',
'http://www.csres.com/sort/chsortdetail/G.html#G10/14',
'http://www.csres.com/sort/chsortdetail/G.html#G15/19',
'http://www.csres.com/sort/chsortdetail/G.html#G20/29',
'http://www.csres.com/sort/chsortdetail/G.html#G30/39',
'http://www.csres.com/sort/chsortdetail/G.html#G40/49',
'http://www.csres.com/sort/chsortdetail/G.html#G50/59',
'http://www.csres.com/sort/chsortdetail/G.html#G60/69',
'http://www.csres.com/sort/chsortdetail/G.html#G70/79',
'http://www.csres.com/sort/chsortdetail/G.html#G80/84',
'http://www.csres.com/sort/chsortdetail/G.html#G85/89',
'http://www.csres.com/sort/chsortdetail/G.html#G90/99',
'http://www.csres.com/sort/chsortdetail/H.html#H00/09',
'http://www.csres.com/sort/chsortdetail/H.html#H10/19',
'http://www.csres.com/sort/chsortdetail/H.html#H10/29',
'http://www.csres.com/sort/chsortdetail/H.html#H20/29',
'http://www.csres.com/sort/chsortdetail/H.html#H30/34',
'http://www.csres.com/sort/chsortdetail/H.html#H30/39',
'http://www.csres.com/sort/chsortdetail/H.html#H40/49',
'http://www.csres.com/sort/chsortdetail/H.html#H40/59',
'http://www.csres.com/sort/chsortdetail/H.html#H50/59',
'http://www.csres.com/sort/chsortdetail/H.html#H60/69',
'http://www.csres.com/sort/chsortdetail/H.html#H70/74',
'http://www.csres.com/sort/chsortdetail/H.html#H70/89',
'http://www.csres.com/sort/chsortdetail/H.html#H80/84',
'http://www.csres.com/sort/chsortdetail/H.html#H90/99',
'http://www.csres.com/sort/chsortdetail/J.html#J00/09',
'http://www.csres.com/sort/chsortdetail/J.html#J10/29',
'http://www.csres.com/sort/chsortdetail/J.html#J30/39',
'http://www.csres.com/sort/chsortdetail/J.html#J40/49',
'http://www.csres.com/sort/chsortdetail/J.html#J50/59',
'http://www.csres.com/sort/chsortdetail/J.html#J60/69',
'http://www.csres.com/sort/chsortdetail/J.html#J70/89',
'http://www.csres.com/sort/chsortdetail/J.html#J90/99',
'http://www.csres.com/sort/chsortdetail/K.html#K00/09',
'http://www.csres.com/sort/chsortdetail/K.html#K10/19',
'http://www.csres.com/sort/chsortdetail/K.html#K20/29',
'http://www.csres.com/sort/chsortdetail/K.html#K30/39',
'http://www.csres.com/sort/chsortdetail/K.html#K40/49',
'http://www.csres.com/sort/chsortdetail/K.html#K50/59',
'http://www.csres.com/sort/chsortdetail/K.html#K60/69',
'http://www.csres.com/sort/chsortdetail/K.html#K70/79',
'http://www.csres.com/sort/chsortdetail/K.html#K80/89',
'http://www.csres.com/sort/chsortdetail/K.html#K90/99',
'http://www.csres.com/sort/chsortdetail/L.html#L00/09',
'http://www.csres.com/sort/chsortdetail/L.html#L10/34',
'http://www.csres.com/sort/chsortdetail/L.html#L35/39',
'http://www.csres.com/sort/chsortdetail/L.html#L40/49',
'http://www.csres.com/sort/chsortdetail/L.html#L50/54',
'http://www.csres.com/sort/chsortdetail/L.html#L55/59',
'http://www.csres.com/sort/chsortdetail/L.html#L60/69',
'http://www.csres.com/sort/chsortdetail/L.html#L70/84',
'http://www.csres.com/sort/chsortdetail/L.html#L85/89',
'http://www.csres.com/sort/chsortdetail/L.html#L90/94',
'http://www.csres.com/sort/chsortdetail/L.html#L95/99',
'http://www.csres.com/sort/chsortdetail/M.html#M00/09',
'http://www.csres.com/sort/chsortdetail/M.html#M10/29',
'http://www.csres.com/sort/chsortdetail/M.html#M30/49',
'http://www.csres.com/sort/chsortdetail/M.html#M50/59',
'http://www.csres.com/sort/chsortdetail/M.html#M60/69',
'http://www.csres.com/sort/chsortdetail/M.html#M70/79',
'http://www.csres.com/sort/chsortdetail/M.html#M80/89',
'http://www.csres.com/sort/chsortdetail/M.html#M90/99',
'http://www.csres.com/sort/chsortdetail/N.html#N00/09',
'http://www.csres.com/sort/chsortdetail/N.html#N10/19',
'http://www.csres.com/sort/chsortdetail/N.html#N20/29',
'http://www.csres.com/sort/chsortdetail/N.html#N30/39',
'http://www.csres.com/sort/chsortdetail/N.html#N40/49',
'http://www.csres.com/sort/chsortdetail/N.html#N50/59',
'http://www.csres.com/sort/chsortdetail/N.html#N60/69',
'http://www.csres.com/sort/chsortdetail/N.html#N70/79',
'http://www.csres.com/sort/chsortdetail/N.html#N90/99',
'http://www.csres.com/sort/chsortdetail/P.html#P00/09',
'http://www.csres.com/sort/chsortdetail/P.html#P10/14',
'http://www.csres.com/sort/chsortdetail/P.html#P15/19',
'http://www.csres.com/sort/chsortdetail/P.html#P20/29',
'http://www.csres.com/sort/chsortdetail/P.html#P30/39',
'http://www.csres.com/sort/chsortdetail/P.html#P40/44',
'http://www.csres.com/sort/chsortdetail/P.html#P45/49',
'http://www.csres.com/sort/chsortdetail/P.html#P50/54',
'http://www.csres.com/sort/chsortdetail/P.html#P55/59',
'http://www.csres.com/sort/chsortdetail/P.html#P60/64',
'http://www.csres.com/sort/chsortdetail/P.html#P65/69',
'http://www.csres.com/sort/chsortdetail/P.html#P70/79',
'http://www.csres.com/sort/chsortdetail/P.html#P80/84',
'http://www.csres.com/sort/chsortdetail/P.html#P85/89',
'http://www.csres.com/sort/chsortdetail/P.html#P90/94',
'http://www.csres.com/sort/chsortdetail/P.html#P95/99',
'http://www.csres.com/sort/chsortdetail/Q.html#Q00/09',
'http://www.csres.com/sort/chsortdetail/Q.html#Q10/29',
'http://www.csres.com/sort/chsortdetail/Q.html#Q30/39',
'http://www.csres.com/sort/chsortdetail/Q.html#Q40/49',
'http://www.csres.com/sort/chsortdetail/Q.html#Q50/59',
'http://www.csres.com/sort/chsortdetail/Q.html#Q60/69',
'http://www.csres.com/sort/chsortdetail/Q.html#Q70/79',
'http://www.csres.com/sort/chsortdetail/Q.html#Q80/89',
'http://www.csres.com/sort/chsortdetail/Q.html#Q90/99',
'http://www.csres.com/sort/chsortdetail/R.html#R00/09',
'http://www.csres.com/sort/chsortdetail/R.html#R10/19',
'http://www.csres.com/sort/chsortdetail/R.html#R20/29',
'http://www.csres.com/sort/chsortdetail/R.html#R30/39',
'http://www.csres.com/sort/chsortdetail/R.html#R40/49',
'http://www.csres.com/sort/chsortdetail/R.html#R50/59',
'http://www.csres.com/sort/chsortdetail/R.html#R60/69',
'http://www.csres.com/sort/chsortdetail/R.html#R80/89',
'http://www.csres.com/sort/chsortdetail/S.html#S00/09',
'http://www.csres.com/sort/chsortdetail/S.html#S10/29',
'http://www.csres.com/sort/chsortdetail/S.html#S30/39',
'http://www.csres.com/sort/chsortdetail/S.html#S40/49',
'http://www.csres.com/sort/chsortdetail/S.html#S50/59',
'http://www.csres.com/sort/chsortdetail/S.html#S60/69',
'http://www.csres.com/sort/chsortdetail/S.html#S70/79',
'http://www.csres.com/sort/chsortdetail/S.html#S80/84',
'http://www.csres.com/sort/chsortdetail/S.html#S90/99',
'http://www.csres.com/sort/chsortdetail/T.html#T00/09',
'http://www.csres.com/sort/chsortdetail/T.html#T10/19',
'http://www.csres.com/sort/chsortdetail/T.html#T20/29',
'http://www.csres.com/sort/chsortdetail/T.html#T30/34',
'http://www.csres.com/sort/chsortdetail/T.html#T35/39',
'http://www.csres.com/sort/chsortdetail/T.html#T40/49',
'http://www.csres.com/sort/chsortdetail/T.html#T50/59',
'http://www.csres.com/sort/chsortdetail/T.html#T60/69',
'http://www.csres.com/sort/chsortdetail/T.html#T70/79',
'http://www.csres.com/sort/chsortdetail/T.html#T80/89',
'http://www.csres.com/sort/chsortdetail/T.html#T90/99',
'http://www.csres.com/sort/chsortdetail/U.html#U00/09',
'http://www.csres.com/sort/chsortdetail/U.html#U10/19',
'http://www.csres.com/sort/chsortdetail/U.html#U20/29',
'http://www.csres.com/sort/chsortdetail/U.html#U30/39',
'http://www.csres.com/sort/chsortdetail/U.html#U40/49',
'http://www.csres.com/sort/chsortdetail/U.html#U50/59',
'http://www.csres.com/sort/chsortdetail/U.html#U60/69',
'http://www.csres.com/sort/chsortdetail/U.html#U80/89',
'http://www.csres.com/sort/chsortdetail/U.html#U90/99',
'http://www.csres.com/sort/chsortdetail/V.html#V00/09',
'http://www.csres.com/sort/chsortdetail/V.html#V10/19',
'http://www.csres.com/sort/chsortdetail/V.html#V20/29',
'http://www.csres.com/sort/chsortdetail/V.html#V30/34',
'http://www.csres.com/sort/chsortdetail/V.html#V35/49',
'http://www.csres.com/sort/chsortdetail/V.html#V50/59',
'http://www.csres.com/sort/chsortdetail/V.html#V70/79',
'http://www.csres.com/sort/chsortdetail/V.html#V80/89',
'http://www.csres.com/sort/chsortdetail/V.html#V90/99',
'http://www.csres.com/sort/chsortdetail/W.html#W00/09',
'http://www.csres.com/sort/chsortdetail/W.html#W10/19',
'http://www.csres.com/sort/chsortdetail/W.html#W20/29',
'http://www.csres.com/sort/chsortdetail/W.html#W30/39',
'http://www.csres.com/sort/chsortdetail/W.html#W40/49',
'http://www.csres.com/sort/chsortdetail/W.html#W50/54',
'http://www.csres.com/sort/chsortdetail/W.html#W55/59',
'http://www.csres.com/sort/chsortdetail/W.html#W60/69',
'http://www.csres.com/sort/chsortdetail/W.html#W70/79',
'http://www.csres.com/sort/chsortdetail/W.html#W90/99',
'http://www.csres.com/sort/chsortdetail/X.html#X00/09',
'http://www.csres.com/sort/chsortdetail/X.html#X10/29',
'http://www.csres.com/sort/chsortdetail/X.html#X30/34',
'http://www.csres.com/sort/chsortdetail/X.html#X35/39',
'http://www.csres.com/sort/chsortdetail/X.html#X40/49',
'http://www.csres.com/sort/chsortdetail/X.html#X50/59',
'http://www.csres.com/sort/chsortdetail/X.html#X60/69',
'http://www.csres.com/sort/chsortdetail/X.html#X70/79',
'http://www.csres.com/sort/chsortdetail/X.html#X80/84',
'http://www.csres.com/sort/chsortdetail/X.html#X85/89',
'http://www.csres.com/sort/chsortdetail/X.html#X90/99',
'http://www.csres.com/sort/chsortdetail/Y.html#Y00/09',
'http://www.csres.com/sort/chsortdetail/Y.html#Y10/19',
'http://www.csres.com/sort/chsortdetail/Y.html#Y20/29',
'http://www.csres.com/sort/chsortdetail/Y.html#Y30/39',
'http://www.csres.com/sort/chsortdetail/Y.html#Y40/44',
'http://www.csres.com/sort/chsortdetail/Y.html#Y45/49',
'http://www.csres.com/sort/chsortdetail/Y.html#Y50/59',
'http://www.csres.com/sort/chsortdetail/Y.html#Y60/69',
'http://www.csres.com/sort/chsortdetail/Y.html#Y70/74',
'http://www.csres.com/sort/chsortdetail/Y.html#Y75/79',
'http://www.csres.com/sort/chsortdetail/Y.html#Y80/84',
'http://www.csres.com/sort/chsortdetail/Y.html#Y85/89',
'http://www.csres.com/sort/chsortdetail/Y.html#Y90/98',
'http://www.csres.com/sort/chsortdetail/Z.html#Z00/09',
'http://www.csres.com/sort/chsortdetail/Z.html#Z10/39',
'http://www.csres.com/sort/chsortdetail/Z.html#Z50/59',
'http://www.csres.com/sort/chsortdetail/Z.html#Z60/79']
    start_urls = [random.choice(urls)]



    baseurl = "http://www.csres.com"
    #start_urls = StartURL.startURL


    def parse(self, response):
        #提取二级标题,去重
        one_list = response.xpath("//tr/td/a[@class='sh14lian']/@href").extract()
        a = set(one_list)
        a = list(a)
        a.remove("/sort/Chtype/_1.html")
        #one_list.remove("/sort/Chtype/_1.html")
        for biaozhunURL in a:

            url = self.baseurl + biaozhunURL
            print "[LOG:]"+ url + "###############################################"
            yield scrapy.Request(url, callback=self.parse_one)
            #time.sleep(0.2)

    def parse_one(self,response):
        #提取详情页面,并发送下一页请求
        two_list = response.xpath("//td[2]/a[@target='_blank']/font[@color='#000000']/../@href").extract()
        for biaoti in two_list:
            url = self.baseurl + biaoti
            print "[LOG:]" + url + "================================="
            yield scrapy.Request(url, callback=self.parse_two)
            #time.sleep(2)
            #with open('10.txt', 'a') as f:

                #f.write("'" + url + "'"+","+'\n')

        page = response.xpath(u"//a[@class='lan'][text()='[下一页]']/@href").extract()
        if len(page) > 0:
            nextpage = response.xpath(u"//a[@class='lan'][text()='[下一页]']/@href").extract()[0]
            url2 = self.baseurl + nextpage
            print "[LOG:]" + url2 + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            yield scrapy.Request(url2, callback=self.parse_one)
            #time.sleep(0.2)


    def parse_two(self,response):
        item = BiaozhunItem()
        if len(response.xpath("//td[@width='50%']/font/strong/text()")):
            item['bianhao'] = response.xpath("//td[@width='50%']/font/strong/text()").extract()[0]
        else:
            item['bianhao'] = ""
        if len(response.xpath("//tr/td/h3/text()")):
            item['nname'] = response.xpath("//tr/td/h3/text()").extract()[0]
        else:
            item['nname'] = ""


        if len(response.xpath("//td/a/font/strong/text()")):
            item['bzzhuangtai'] = response.xpath("//td/a/font/strong/text()").extract()[0]
        else:
            item['bzzhuangtai'] = "" 
            #//td/a/font/strong/strong/font/text()


       # if len(response.xpath("//td/a/font/strong/strong/font/text()")):
        #    item['bzzhuangtai'] = response.xpath("//td/a/font/strong/strong/font/text()").extract()[0]
       # else:
        #    item['bzzhuangtai'] = ""

            #//td/a/font/strong/strong/font/text()



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
