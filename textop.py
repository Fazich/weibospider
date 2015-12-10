# -*- coding:utf-8 -*-

class textop(object):
    def textWrite(self,content):
        filehandle = open("data.txt","w")
        filehandle.write(content)
        filehandle.close()


