# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MySQLHelper
   Description :
   Author :       Administrator
   date：          2019/1/19 0019
-------------------------------------------------
   Change Activity:
                   2019/1/19 0019:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''

import MySQLdb

class MySQLHelper:

    def __init__(self):
        __conn = None

    def connetMySQL(self,host=None,user=None,pwd=None,port=3306,charset="utf8"):
        self.__conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=pwd,
            charset=charset
        )
        if None != self.__conn:
            print "Connect to database success.[%s]"%host
            return self.__conn
        else:
            raise "Connect to database fail. [%s]"%host


    def getCursor(self):
        return self.__conn.cursor()

if __name__ == '__main__':
    pass