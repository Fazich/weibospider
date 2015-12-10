# -*- coding:utf-8 -*-
# coding:utf-8

import requests
import BeautifulSoup
import sys
import re
import time
import selenium
# 解决文本注入乱码问题
reload(sys)
sys.setdefaultencoding('utf-8')


class Weibo:
    # 模拟登录
    def login(self, userName, userPassword):
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36"}
        url = "http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2Flis1956&backTitle=%CE%A2%B2%A9&vt="
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup.BeautifulSoup(html)
        password = soup.findAll(type="password")
        for str in password:
            password = str["name"]
        vk = soup.findAll(attrs={'name': 'vk'})
        for str in vk:
            vk = str["value"]

        data = {
            "mobile": userName,
            password: userPassword,
            "remember": "on",
            "backURL": "http%3A%2F%2Fweibo.cn%2F",
            "backTitle": "微博",
            "tryCount": "",
            "vk": vk,
            "submit": "登录"}
        loginReq = requests.post(url, data, headers = header,timeout = 5).text
        soup = BeautifulSoup.BeautifulSoup(loginReq)
        print soup.prettify()
        # self.myweibo(loginReq)

    # 进入我的微博
    def myweibo(self, loginReq):

        loginHtml = loginReq.text
        soupLogin = BeautifulSoup.BeautifulSoup(loginHtml)

        # 获取我的微博栏目的url
        myweibo = soupLogin.find(attrs={"class": "tip2"}).next
        myweiboURL = "http://weibo.cn" + myweibo["href"]
        # print myweiboURL
        # myweiboURL = "http://weibo.cn/lis1956"
        # self.pageflip(myweiboURL)

    # 翻页并将微博写入文本
    def pageflip(self, myweiboURL):
        pageCount = 1
        cookies = {
            "Cookie": "_T_WM=50d280dfe706287e5bda55c8fec88337; SUB=_2A257YQtnDeRxGeRM4lER9i7KyzuIHXVYrZUvrDV6PUJbrdAKLUf3kW1pHLfERtsPvlV6Ugf5GtWrAkiOCA..; gsid_CTandWM=4uPUd1461sy2kaETMqsdf9CwQ9N"}
        myweiboHTML = requests.post(myweiboURL, cookies=cookies).text
        soupmyWeibo = BeautifulSoup.BeautifulSoup(myweiboHTML)

        print soupmyWeibo.prettify()

        # for i in range(1, pageCount):
        #     pageData = {
        #         "mp": pageCount,
        #         "page": i
        #     }
        #     myweiboHTML = requests.post(myweiboURL, data=pageData, cookies=cookies).text
        #     soupmyWeibo = BeautifulSoup.BeautifulSoup(myweiboHTML)
        #     content = soupmyWeibo.findAll(attrs={"class": "ctt"})
        #
        #     # a为不删除原内容持续写入
        #     # filehandle = open("data.txt", "a")
        #     for tag in content:
        #         tagcontent = tag.text
        #         print tagcontent
        #         # filehandle.write(tagcontent + "\n")
        #
        #     # filehandle.close()



    # 爬取用户资料
    def userInfo(self):
        cookies = {
            "Cookie": " _T_WM=f5b89549bbf0e5150dc56a1c045a188f; SUHB=0ebcnsIKZFuZ_Q; SUB=_2A257ZriyDeRxGeRM4lER9i7KyzuIHXVYqNj6rDV6PUJbrdANLRb2kW0QN5fFe2tslKrefpsqwOKgmUDaCg..; gsid_CTandWM=4uGcd1461AYDSv66Tc97w9CwQ9N"}
        # startUserID = 1821461481
        startUserId = 1000005885
        filehandle = open("userInfo.txt", "a")

        for startUserId in range(startUserId, 1000010000):
            # 设置遍历访问时间缓冲
            # time.sleep(0.3)

            infoURL = "http://weibo.cn/" + str(startUserId) + "/info"
            # 爬虫异常时的操作
            try:
                reqInfo = requests.get(infoURL, cookies=cookies)
            except:
                print "超时"
                # filehandle.close()
            print "正在遍历第"+str(startUserId)+"号用户"
            # print reqInfo.status_code
            infoText = reqInfo.text
            infoSoup = BeautifulSoup.BeautifulSoup(infoText)
            target = infoSoup.findAll(attrs={"class": "c"})
            for tag in target:
                tagContent = tag.text
                reg = re.compile(r'生日:(\d{4})')
                # print tagContent
                birthday = re.findall(reg, str(tagContent))
                # print birthday[0]

                if len(birthday):
                    # print type(birthday)
                    print "第"+str(startUserId)+"号用户生日为:"+birthday[0]
                    if (int(birthday[0]) >= 1994):
                        print "第"+str(startUserId)+"号用户符合要求，生日："+birthday[0]+" "+infoURL
                        filehandle.write(infoURL + " " + birthday[0] + "\n")

        filehandle.close()
        # print birthday

        # content = str(tagContent)
        # print type(content)


spider = Weibo()
spider.login("512185256@qq.com", "05599123abc")
# spider.userInfo()
#
# content = "昵称:津JSH866_642性别:男地区:天津 河东区生日:1979-08-14"
# p = re.compile(r'生日:(\d{4})')
# reg = re.findall(p,str(content))[0]
# print reg
# if reg<1992:
#     print success
# req = requests.get("http://www.baidu.com")
# print req.content