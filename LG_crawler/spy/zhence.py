#coding=utf-8
#这个是全国一的
import requests
import base64
import urllib
import json
from MySQLdb import *
import time
import sys
import hashlib
import time

#reload(sys)
#sys.setdefaultencoding("utf-8")

baseurl = "http://xxgk.miit.gov.cn/gdnps/searchIndex.jsp?params="

url = '''{"goPage":1,"orderBy":[{"orderBy":"publishTime","reverse":true},{"orderBy":"orderTime","reverse":true}],"pageSize":10,"queryParam":[{},{},{"shortName":"fbjg","value":"/1/29/1146295/1652858/1652930"}]}'''
num = 1
#循环爬取所有政策
while num<358:
    uu = url.replace('"goPage":1','"goPage":%s'%num)
    print uu
    u = urllib.quote(uu)
    u = urllib.quote(u)
    #print u
    headers={"Content-Type": "application/json",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; OPPO R9 Plustm A Build/MMB29M)",
            }

    #发送请求
    response = requests.get(baseurl + u, headers = headers)
    #构造json数据
    jsonobj = response.text.replace("({","{").replace("});","}")

    #print jsonobj
    result = json.loads(jsonobj)
    print "正在爬取数据..."
    result_list = result["resultMap"]
    for i in result_list:
        content = i['htmlContent']
        title = i['title']
        m2 = hashlib.md5()   
        m2.update(title.encode("utf-8"))   
        md5 = m2.hexdigest()
        a = i['publishTime'][0:8]
        times = a[:4] + "-" + a[4:6] + "-" + a[6:]
        #时间校验
        try:
            time.strptime(times, "%Y-%m-%d")
            timejiao = times
        except:
            timejiao = ""

        yuan = "中华人民共和国工业和信息化部"
        province = "全国"
        #boost = 0
        #保存到数据库
        try:
            conn = connect(host='192.168.1.207', port=3308, db='policy', user='yangchaoming', passwd='ycm@2017',
                           charset='utf8')
            cur = conn.cursor()
            # count = cs1.execute("insert into test(wenshuid) values('wenshuid')")
            sql = "INSERT ignore INTO policy(content,title,time,yuan,province,md5) VALUES(%s,%s,%s,%s,%s,%s);"

            cur.execute(sql, (content,title,timejiao,yuan,province,md5))
            # print count
            conn.commit()
        except Exception, e:
            print e
        finally:
            cur.close()
            conn.close()
    num += 1
