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
        __host=None
        __port=3306
        __user=None
        __pwd=None
        __dbname=None
        __charset="utf8"
        __cursor = None
        __conn = None

    def connetMySQL(self,host=None,user=None,pwd=None,dbname=None,port=3306,encoding="utf8"):
        if None!=host and ""!=host:
            self.__host=host
        if None !=port and ""!=host:
            self.__port=port
        if None !=user and "" !=user:
            self.__user=user
        if None !=pwd and ""!=pwd:
            self.__pwd=pwd
        if None!=dbname and ""!=dbname:
            self.__dbname=dbname
        if None !=encoding and ""!=encoding:
            self.__charset=encoding

        self.__conn= MySQLdb.connect(
            self.__host,
            self.__user,
            self.__pwd,
            self.__dbname,
            self.__port,
            self.__charset
        )
        return self.__conn

    def getCursor(self):
        self.__cursor=self.__conn.cursor()
        return self.__cursor

    def execute(self,sql,args=None):

        try:
            self.getCursor()
            print self.__cursor
            # 执行sql语句
            result=self.__cursor.execute(sql,args)
            print  result
            # 提交到数据库执行
            self.__conn.commit()
        except Exception as e:
            # Rollback in case there is any error
            self.__conn.rollback()

    def fetchall(self,sql,args=None):
        try:
            self.execute(sql,args)
            return self.__cursor.fetchall()
        except Exception as e:
            print "=======Exception"
            self.closeConnet()

    def getOneData(self,sql):
        self.getCursor()
        print self.__cursor
        # 执行sql语句
        self.__cursor.execute(sql)
        # 使用 fetchone() 方法获取一条数据
        data = self.__cursor.fetchone()

        print "Database version : %s " % data

    def closeConnet(self):
        self.__conn.close()

if __name__ == '__main__':
    pass