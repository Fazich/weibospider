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
    def access(self,url,page_count):
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
            "Cookie": "_T_WM=f5b89549bbf0e5150dc56a1c045a188f; SUHB=0M2FhK0dmMkjh9; SUB=_2A257aWd5DeRxGeRM4lER9i7KyzuIHXVYkgkxrDV6PUJbrdANLVXjkW2OvoUyss3TQI1e3qP8LpZNiMosDQ..; gsid_CTandWM=4uNtd1461H9y4oAC6brMz9CwQ9N; M_WEIBOCN_PARAMS=luicode%3D20000174"
        }
        url = url
        # req = requests.get(url, headers = header,timeout = 5).content

        pageCount = page_count
        fileContent = open("content.txt","a")
        fileAttitude = open("attitude.txt","a")
        fileRepost = open("repost.txt","a")
        fileComment = open("comment.txt","a")
        fileTime = open("time.txt","a")
        for pageStart in range(1,page_count+1):

            pageData = {"mp":pageCount,
            "page":pageStart}
            print "当前页码:"+str(pageStart)
            pageReq = requests.post(url,data = pageData, headers= header, timeout = 5)
            pageHtml = pageReq.text
            if len(pageHtml):
                print "页面加载成功，已完成"+str(round(((pageStart+0.0)/pageCount)*100,2))+"%"
            else:
                print "页面无内容"
                exit()
            soup = BeautifulSoup(pageHtml,"html.parser")
            # 输出网页html判断登录cookie是否过期
            # print soup.prettify()
            # 遍历内容
            targetContent = soup.find_all("span",attrs={"class":"ctt"})
            for tagContent in targetContent:
                # print tagContent.text
                fileContent.write(tagContent.text+"\n")
            # 遍历微博赞
            targetAttitude = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/attitude")})
            for tagAttitude in targetAttitude:
                attitude = str(tagAttitude.text)
                # print  attitude
                regAttitude = re.compile("\D")
                result = re.sub(regAttitude,"",attitude)
                fileAttitude.write(result+"\n")
            # 遍历转发
            targetRepost = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/repost/")})
            for tagRepost in targetRepost:
                repost = str(tagRepost.text)
                # print repost
                regRepost = re.compile("\D")
                result = re.sub(regRepost,"",repost)
                # print result
                fileRepost.write(result+"\n")
            # 遍历评论
            targetComment = soup.find_all("a",attrs={"href":re.compile("http://weibo.cn/comment/")})
            for tagComment in targetComment:
                comment = str(tagComment.text)
                # print comment
                regSource = re.compile("原文评论.*")
                if len(re.findall(regSource,comment)):
                    # print "已删除原文评论信息"
                    pass
                else:
                    # print comment
                    finalComment = re.sub(re.compile("\D"),"",comment)
                    fileComment.write(finalComment+"\n")
            # 遍历时间
            targetTime = soup.find_all("span",attrs={"class":"ct"})
            for tagTime in targetTime:
                time = str(tagTime.text)
                # print time
                regTime = re.compile('来自.*')
                result = re.sub(regTime,"",time)
                # print result
                fileTime.write(result+"\n")
        fileContent.close()
        fileAttitude.close()
        fileRepost.close()
        fileComment.close()
        fileTime.close()
weibo = weibo()
weibo.access('http://weibo.cn/yinqiaochun',410)
# content = "03月07日 00:40 来自JiaThis分享按钮"
# reg = re.compile("来自.*")
# result = re.search(reg,content).group()
# print result

# for start in range(114,115):
#     print start
url = "http://weibo.cn/u/3504018477"

# req = requests.get(url).text
# jsonDict = json.loads(req)
# print jsonDict