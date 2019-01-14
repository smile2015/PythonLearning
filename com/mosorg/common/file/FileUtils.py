# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FileUtils
   Description :
   Author :       Administrator
   date：          2019/1/14 0014
-------------------------------------------------
   Change Activity:
                   2019/1/14 0014:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class FileUtils:

    def __init__(self):
        self.file=None

    def open_file(self,file_path,mode=None):
        self.file = open(file_path, mode)
        return self.file;

    def close_file(self):
        self.file.close()

    def read_lines(self,size=None):
        return self.file.readlines(size)

    def read_line(self,size=None):
        return self.file.readline(size)

