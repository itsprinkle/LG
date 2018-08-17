#coding=utf-8
import requests
import random
import base64
import time


class RandomProxy(object):
    def __init__(self):
        self.num = 0

    def process_request(self):
        while self.num < 50:
            proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=937080193414252&num=100&sep=1"
            proxy_list = requests.get(proxy_api).text.split()
            # 发送代理api请求，获取代理列表
            #self.proxy_list = requests.get(self.proxy_api).text.split()
            #print proxy_list
            #print type(proxy_list)
            #self.num = 0
            #print self.num
            self.num += 1
            # 在代理列表里随机选择一个代理
            proxy = random.choice(proxy_list)
            print proxy + "------------------------------------------"
            #request.meta['proxy'] = "http://" + "122.114.235.252:16816"
            #time.sleep(3600)
            # 对代理验证信息进行base64编码
            # base64_userpass = base64.b64encode(self.proxy_auth)
            # 在请求里添加代理
            #request.meta['proxy'] = "http://" + proxy

            #request.meta['proxy'] = "http://" + "122.114.235.252:16816"
            # 添加代理验证信息
            #request.headers['Proxy-Authorization'] = "Basic " + base64_userpass
if __name__ == "__main__":
    tieba = RandomProxy()
    tieba.process_request()