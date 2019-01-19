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
        __cursor = None

    def connetMySQL(self,host=None,user=None,pwd=None,dbname=None,port=3306,charset="utf8"):
        self.__conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=pwd,
            db=dbname,
            charset=charset
        )
        if None != self.__conn:
            print "Connect to database success.[%s]"%host
            return self.__conn
        else:
            raise "Connect to database fail. [%s]"%host

    def getCursor(self):
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    def execute(self,sql, args=None):
        try:
            self.getCursor()
            # 使用execute方法执行SQL语句
            self.__cursor.execute(sql, args)
            return True
        except Exception as e:
            print str(e)
            return False

    def query(self,sql, args=None):
        try:
            self.getCursor()
            # 使用execute方法执行SQL语句
            self.__cursor.execute(sql, args)
            rs = self.__cursor.fetchall()
            return rs
        except Exception as e:
            print str(e)
            return False

    def commit(self):
        # 提交事务
        self.__conn.commit()

    def closeCursor(self):
        self.__cursor.close()

    def closeConnet(self):
        self.__conn.close()

if __name__ == '__main__':
    pass