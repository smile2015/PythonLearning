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
        self.host=None
        self.port=3306
        self.user=None
        self.pwd=None
        self.dbname=None
        self.charset="utf8"
        self.conn=None
        self.cursor=None

    def connetMySQL(self,host=None,user=None,pwd=None,dbname=None,port=3306,encoding="utf8"):
        if None!=host and ""!=host:
            self.host=host
        if None !=port and ""!=host:
            self.port=port
        if None !=user and "" !=user:
            self.user=user
        if None !=pwd and ""!=pwd:
            self.pwd=pwd
        if None!=dbname and ""!=dbname:
            self.dbname=dbname
        if None !=encoding and ""!=encoding:
            self.charset=encoding

        self.conn= MySQLdb.connect(
            self.host,
            self.user,
            self.pwd,
            self.dbname,
            self.port,
            self.charset
        )

    def getCursor(self):
        self.cursor=self.conn.cursor()

    def closeCursor(self):
        self.cursor.close()

    def closeConnet(self):
        self.conn.close()

if __name__ == '__main__':
    pass