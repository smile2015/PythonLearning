# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     readConfig.py
   Description :
   Author :       MyPC
   date：          2019/2/13
-------------------------------------------------
   Change Activity:
                   2019/2/13:
-------------------------------------------------
"""
__author__ = 'MyPC'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''

import os
import codecs
#ConfigParser
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")



class ReadConfig:
    def __init__(self,path):
        if None<>path:
            configPath=path
        print configPath
        print os.path.realpath(__file__)
        print os.path.realpath(__file__)[0]
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

if __name__ == '__main__':
    pass
