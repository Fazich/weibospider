# -*- coding:utf-8 -*-
# coding:utf-8

import requests
from bs4 import BeautifulSoup
import sys
import json
import re
import time
import selenium
# 解决文本注入乱码问题
reload(sys)
sys.setdefaultencoding('utf-8')

class weibo(object):
    def access(self):
        header = {
            "Host": "weibo.cn",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36",
            "Referer": "http://weibo.cn/lis1956",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "_T_WM=50d280dfe706287e5bda55c8fec88337; SUB=_2A257YfBhDeRxGeRM4lER9i7KyzuIHXVYrZAprDV6PUJbrdANLWrkkW0dNR8__ZzLiVo819vIDtuxWXCPJQ..; gsid_CTandWM=4u4xd1461hth2eIiFpurm9CwQ9N"
        }
        url ="http://weibo.cn/lis1956"
        req = requests.get(url, headers = header,timeout = 5).content

        pageCount = 155
        fileContent = open("content.txt","a")
        fileAttitude = open("attitude.txt","a")
        fileRepost = open("repost.txt","a")
        fileComment = open("comment.txt","a")
        fileTime = open("time.txt","a")
        for pageStart in range(118,156):
            pageData = {"mp":pageCount,
            "page":pageStart}
            print "当前页码:"+str(pageStart)
            pageReq = requests.post(url,data = pageData, headers= header, timeout = 5)
            pageHtml = pageReq.text
            soup = BeautifulSoup(pageHtml,"html.parser")
            # print soup.prettify()
            # 遍历内容
            targetContent = soup.find_all("span",attrs={"class":"ctt"})
            for tagContent in targetContent:
                print tagContent.text
                fileContent.write(tagContent.text+"\n")
            # # 遍历微博赞用
            # targetAttitude = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/attitude")})
            # for tagAttitude in targetAttitude:
            #     print tagAttitude.text
            #     fileAttitude.write(tagAttitude.text+"\n")
            # # 遍历转发
            # targetRepost = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/repost/")})
            # for tagRepost in targetRepost:
            #     print tagRepost.text
            #     fileRepost.write(tagRepost.text+"\n")
            # # 遍历评论
            # targetComment = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/comment/")})
            # for tagComment in targetComment:
            #     print tagComment.text
            #     fileComment.write(tagComment.text+"\n")
            # # 便利时间
            # targetTime = soup.find_all("span",attrs={"class":"ct"})
            # for tagTime in targetTime:
            #     print tagTime.text
            #     fileTime.write(tagTime.text+"\n")
        fileContent.close()
        # fileAttitude.close()
        # fileRepost.close()
        # fileComment.close()
        # fileTime.close()
weibo = weibo()
weibo.access()
# for start in range(114,115):
#     print start
url = "http://m.weibo.cn/page/json?containerid=1005051051919207_-_WEIBO_SECOND_PROFILE_WEIBO&page=3"

# req = requests.get(url).text
# jsonDict = json.loads(req)
# print jsonDict