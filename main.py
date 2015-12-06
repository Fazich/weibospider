# -*- coding:utf-8 -*-
# coding:utf-8

import requests
import BeautifulSoup
import re



class Weibo:
    # 模拟登录并进入我的微博
    def login(self,userName,userPassword):
        url = "http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
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
        loginReq = requests.post(url, data)
        self.myweibo(loginReq)

    def myweibo(self, loginReq):

        loginHtml = loginReq.text
        soupLogin = BeautifulSoup.BeautifulSoup(loginHtml)

        # 获取我的微博栏目的url
        myweibo = soupLogin.find(attrs={"class": "tip2"}).next
        myweiboURL = "http://weibo.cn" + myweibo["href"]
        print myweiboURL
        self.pageflip(myweiboURL)

    def pageflip(self, myweiboURL):
        pageCount = 49
        cookies = {
            "Cookie": " _T_WM=f5b89549bbf0e5150dc56a1c045a188f; SUHB=0ebcnsIKZFuZ_Q; SUB=_2A257ZriyDeRxGeRM4lER9i7KyzuIHXVYqNj6rDV6PUJbrdANLRb2kW0QN5fFe2tslKrefpsqwOKgmUDaCg..; gsid_CTandWM=4uGcd1461AYDSv66Tc97w9CwQ9N"}

        for i in range(1, pageCount):
            pageData = {
                "mp": pageCount,
                "page": i
            }
            myweiboHTML = requests.post(myweiboURL, data=pageData, cookies=cookies).text
            soupmyWeibo = BeautifulSoup.BeautifulSoup(myweiboHTML)
            content = soupmyWeibo.findAll(attrs={"class": "ctt"})
            for tag in content:
                print tag.text


spider = Weibo()
spider.login()
