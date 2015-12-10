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


class washData(object):
    def wash(self,RegExp,RegString):
        oldfile = open("content.txt","r+")
        content = oldfile.readlines()
        filehandle = open("content.txt","w+")
        # 清洗url

        for eachLine in content:
            url = re.search(RegExp, eachLine)
            if url:
                eachLine = eachLine.replace(url.group(),"")
                filehandle.write(eachLine)
                print "匹配到"+RegString+url.group()

            else:

                filehandle.write(eachLine)

        print RegString+"匹配执行完毕"
        filehandle.close()

    def saveChinese(self,RegExp,RegString):
        oldfile = open("content.txt","r+")
        content = oldfile.readlines()
        filehandle = open("content.txt","w+")
        # 清洗url

        for eachLine in content:
            result = re.findall(RegExp, eachLine.decode("utf-8"))
            if result:
                eachLine = eachLine.replace(eachLine,"".join(result))
                filehandle.write(eachLine)
                print "匹配到中文:".join(result)

            else:
                print "未匹配到"
                filehandle.write(eachLine)

        print RegString+"匹配执行完毕"
        filehandle.close()




washData = washData()
# url正则
regUrl = re.compile("(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?")
# html特殊编码正则
regHtml = re.compile("&#\d+")
# 邮箱正则
regMail = re.compile("([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+")
# 清除位置信息
regLocation = re.compile("\[位置\].*")
# 表情信息
regExpress = re.compile("\[.*]")
# 删除废弃微博
regDelete = re.compile("抱歉.*")
washData.wash(regMail,"邮箱")
washData.wash(regHtml,"html特殊编码正则")
washData.wash(regUrl,"url正则")
washData.wash(regLocation,"位置信息")
washData.wash(regExpress,"表情信息")
washData.wash(regDelete,"废弃微博")
# 保留中文字符串
xx=u"([\u4e00-\u9fa5]+)"
pattern = re.compile(xx)
washData.saveChinese(pattern,"中文字符")

# source = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3"
# temp = source.decode('utf8')
#
# results =  pattern.findall(temp)
# for result in results :
#   print result

# print u"[\u4e00-\u9fa5]"



# content = "哈啊啊搜破大叔就觉得http://www.baidu.com"
# regUrl = re.compile("(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?")
# url = re.search(regUrl,content)
# newContent = content.replace(url.group(),"")
# print newContent
