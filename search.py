# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import StringIO
import re
import time
import selenium
import HTMLParser
import json
import chardet

reload(sys)
sys.setdefaultencoding('utf-8')

class search(object):
    def search(self):
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36"}
        cookie = {"Cookie": "SINAGLOBAL=8804361869115.383.1431264238066; wvr=6; un=512185256@qq.com; SUS=SID-2293060607-1449463826-GZ-lsirg-7cd514fbb88b24c28421944d6f27354b; SUE=es%3D3f1179e878fa86c22fdf389ece217cf6%26ev%3Dv1%26es2%3D579a3f549bf1b844919a806f297aed5a%26rs0%3DUhQ9ELhOkp57MaTj1%252B4%252FUwEA3OxQGLML96%252FqKXlETLzbtqQQkQqgQBug3lu63QvWEn0OwpI0EOexRDPxH9GoI7Ex%252Fw1boeMOUoZ42ZMU3e3U13%252B%252BeVPtyG877eeeQoDgr89jRYnVm7jHUbehzMgrzcO7kw0PhIhhT55GBORqR38%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1449463826%26et%3D1449550226%26d%3Dc909%26i%3D354b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2293060607%26name%3D512185256%2540qq.com%26nick%3DEbne%26fmp%3D%26lcp%3D2014-05-17%252009%253A30%253A16; SUB=_2A257YWBCDeRxGeRM4lER9i7KyzuIHXVYF9aKrDV8PUNbvtBeLVrzkW8iwjUO7o_SNUkRICO3l2FUK-8V0w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhLygbFuS9AymbY0nh4Sasg5JpX5KMt; SUHB=0cSW5jp3WlkPYK; ALF=1480999825; SSOLoginState=1449463826; SWB=usrmdinst_10; _s_tentry=weibo.com; Apache=2374435586389.1543.1449463836024; ULV=1449463836073:45:7:4:2374435586389.1543.1449463836024:1449408936880; WBStore=5955be0e3d5411da|undefined; UOR=www.3lian.com,widget.weibo.com,www.pythoner.cn; ULOGIN_IMG=14494796455905"}
        pageCount = 1
        filehandle = open("userInfo.txt", "a")
        for i in range(1,pageCount):
            url = "http://s.weibo.com/user/&tag=%E5%AD%A6%E7%94%9F&age=18y&auth=ord&page="+str(i)
            req = requests.get(url, cookies = cookie, headers = header)
            # time.sleep(2)
            # 解析嵌入到页面里js脚本
            soup = BeautifulSoup(req.text,"html.parser")
            print req.status_code
            script = soup.find_all("script",text=re.compile("STK"))
            # 遍历脚本内容并解码

            print script
            for tag in script:
                targetContent = tag.text.decode('unicode-escape').encode('utf-8').replace('\\','')
                targetSoup = BeautifulSoup(targetContent,"html.parser")
                # 检索解码后的目标DOM
                print targetSoup
                targetName = targetSoup.find_all(attrs={"class":"W_texta W_fb"})
                for tag in targetName:
                    if(len(tag)):
                        targetContent = tag.text+"URl:"+tag["href"]
                        # print tag.text+"URl:"+tag["href"]
                        print targetContent
                        filehandle.write(targetContent + "\n")

        filehandle.close()








search = search()
search.search()
code = "\u4f60\u597d"
# print code.decode("unicode-escape")
# code = "&lt;div &gt;"
# print type(code)
# codeTxt = code.decode('unicode_escape').encode("utf-8")
# soup = BeautifulSoup(codeTxt,"html.parser")
# print soup.find_all(text="你好")[0]
