#coding=utf-8
#这个是全国二的
import requests
import base64
import urllib
import json
from MySQLdb import *
import time
import sys
from lxml import etree
import re
import hashlib
import time


reload(sys)
sys.setdefaultencoding("utf-8")
class ZhenceSpider():

    def __init__(self):
        #所有的url
        self.baseurl_list = ["http://www.miit.gov.cn/n1146295/n1146562/n1146650/index.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_1.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_2.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_3.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_4.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_5.html","http://www.miit.gov.cn/n1146295/n1146562/n1146650/index_1274883_6.html"]
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
        self.offset = 0
    #发送请求
    def send(self):
        for i in self.baseurl_list:
            response = requests.get(i, headers=self.headers).content
            html = etree.HTML(response)
            urllist = html.xpath("//li/a/@href")
            self.sendtwo(urllist)
    #解析数据
    def sendtwo(self,urllist):
        #item = []
        for i in urllist:
            url = "http://www.miit.gov.cn" + i[8:]
            response = requests.get(url, headers=self.headers).content
            html = etree.HTML(response)
            title = html.xpath("//h1/text()")[0]
            m2 = hashlib.md5()   
            m2.update(title.encode("utf-8"))   
            md5 = m2.hexdigest()
            #print title
            #item.append(title)
            a = html.xpath("//span[@id='con_time']/text()")[0]
            times = re.findall(r"\d.*\d", a)[0]
            try:
                time.strptime(times, "%Y-%m-%d")
                timejiao = times
            except:
                timejiao = ""
            #print time[5:]
            contentt = html.xpath("//div[@class='ccontent center']")[0]
            #item.append(content)
            #print item
            #print content
            content = etree.tostring(contentt, pretty_print=True)
            yuan = "中华人民共和国工业和信息化部"
            province = "全国"
            print "正在爬取数据..."
            #boost = 0
            try:
                conn = connect(host='192.168.1.207', port=3308, db='policy', user='yangchaoming', passwd='ycm@2017',
                               charset='utf8')
                cur = conn.cursor()
                # count = cs1.execute("insert into test(wenshuid) values('wenshuid')")
                sql = "INSERT ignore INTO policy(content,title,time,yuan,province,md5) VALUES(%s,%s,%s,%s,%s,%s);"

                cur.execute(sql, (content, title, timejiao, yuan,province,md5))
                # print count
                conn.commit()
            except Exception, e:
                print e
            finally:
                cur.close()
                conn.close()

            #time.sleep(3)

if __name__ == "__main__":
    spider = ZhenceSpider()
    spider.send()


