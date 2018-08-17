# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from settings import USER_AGENT_LIST
import requests
import random
import base64
import time
import redis


# User-Agetn 下载中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        user_agent = random.choice(USER_AGENT_LIST)
        # date = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        #print user_agent
        request.headers.setdefault('User-Agent', user_agent)
        #request.headers.setdefault('If-Modified-Since', date)


class RandomProxy(object):
    # def __init__(self):
    #     #self.num = 0
    #     # 代理验证信息
    #     #self.proxy_auth = "mr_mao_hacker:sffqry9r"
    #     # 代理api接口
    #     #self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=1&dedup=1&format=json&sep=1"
    #     # 发送代理api请求，获取代理列表
    #     #self.proxy_list = requests.get(self.proxy_api).text.split()
    #     self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=3&sep=1"
    #     self.proxy_list = requests.get(self.proxy_api).text.split()
    #     #self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=3&sep=1"
    #     #self.proxy_list = requests.get(self.proxy_api).text.split()
    #
    # def process_response(self, request, response,spider):
    #     if response.status != 200:
    #         # 发送代理api请求，获取代理列表
    #         self.proxy_list = requests.get(self.proxy_api).text.split()
    #
    #         print self.proxy_list
    #         #self.num = 0
    #         #print self.num
    #         #self.num += 1
    #         # 在代理列表里随机选择一个代理
    #
    #     proxy = random.choice(self.proxy_list)
    #     print proxy + "---------------------------------------------------------------------------------"
    #         # 对代理验证信息进行base64编码
    #         #base64_userpass = base64.b64encode(self.proxy_auth)
    #         # 在请求里添加代理
    #     request.meta['proxy'] = "http://" + proxy
            #time.sleep(20)
            # request.meta['proxy'] = "http://" + "60.255.186.169:8888"
            # 添加代理验证信息
            #request.headers['Proxy-Authorization'] = "Basic " + ""
            #time.sleep(1000)
    #     #return request
    #     #return response
    import random
    import scrapy
    from scrapy import log

    # logger = logging.getLogger()



    # def process_request(self, request, spider):
    #     '''对request对象加上proxy'''
    #     proxy = self.get_random_proxy()
    #     print("this is request ip:" + proxy)
    #     request.meta['proxy'] = "http://" + proxy
    #
    # def process_response(self, request, response, spider):
    #     '''对返回的response处理'''
    #     # 如果返回的response状态不是200，重新生成当前request对象
    #     if response.status != 200:
    #         proxy = self.get_random_proxy()
    #         print("this is response ip:" + proxy)
    #         # 对当前reque加上代理
    #         request.meta['proxy'] = proxy
    #         return request
    #     return response
    #
    # def get_random_proxy(self):
    #     '''随机从文件中读取proxy'''
    #
    #     proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=3&sep=1"
    #     proxy_list = requests.get(proxy_api).text.split()
    #     proxy = random.choice(proxy_list)
    #     return proxy



    def bbb(self):
        #r = requests.get('http://47.93.30.165:8000/')
        #a = r.text
        #proxies = {"http": "http://" + a}
        pass
        #r1 = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
        #return r1
        #self.num = 0
        # 代理验证信息
        #self.proxy_auth = "mr_mao_hacker:sffqry9r"
        # 代理api接口
        #self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=3&sep=1"
        # 发送代理api请求，获取代理列表
        #self.proxy_list = requests.get(self.proxy_api).text.split()


    def process_request(self, request, spider):
        r = requests.get('http://0.0.0.0:8000/')
        a = r.text
        print a
        #proxies = {"http": "http://" + a}

        #r1 = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
        #print r1
        #r = redis.Redis(host='47.93.30.165', port='6379', password='111111')
        #proxy = r.get('adsl')
        #print proxy
        #proxy = r1
        request.meta['proxy'] = "http://" + a




        # if self.num > 100:
        #     #发送代理api请求，获取代理列表
        #     self.proxy_list = requests.get(self.proxy_api).text.split()
        #     print self.proxy_list
        #     self.num = 0
        # print self.num
        # self.num += 1
        # #在代理列表里随机选择一个代理
        # proxy = random.choice(self.proxy_list)
        #
        # #对代理验证信息进行base64编码
        # #base64_userpass = base64.b64encode(self.proxy_auth)
        # #在请求里添加代理

        #time.sleep(1)

        #request.meta['proxy'] = "http://" + "36.251.248.76:80"
        #添加代理验证信息
        #request.headers['Proxy-Authorization'] = "Basic " + base64_userpass

    # def process_response(self, request, response, spider):
    #
    #     '''对返回的response处理'''
    #     # 如果返回的response状态不是200，重新生成当前request对象
    #     if response.status != 200:
    #         self.proxy_list = requests.get(self.proxy_api).text.split()
    #         proxy = random.choice(self.proxy_list)
    #         #proxy = self.get_random_proxy()
    #         print("this is response ip:" + proxy)
    #         # 对当前reque加上代理
    #         request.meta['proxy'] = proxy
    #         return request
    #     return response