# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PropertiesUtils
   Description :
   Author :       Administrator
   date：          2019/1/13 0013
-------------------------------------------------
   Change Activity:
                   2019/1/13 0013:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys
reload(sys)
default_encoding="utf-8"
if(default_encoding!=sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import re
import os
import tempfile

'''
自动加载pythonSripts/目录下的properties
'''



class PropertiesUtils:

    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        self.loadProperties()

    def loadProperties1(self):
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception, e:
            raise e
        else:
            fopen.close()

    def loadProperties(self):
        with open(self.file_name, 'r') as fopen:
            for line in fopen.readlines():
                line = line.strip() # 把末尾的'\n'删掉
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()


    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            default_value=self.properties[key]
            #print default_value
            return default_value
        return default_value

    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '=.*', key + '=' + value, True)


def parse(file_name):
    return PropertiesUtils(file_name)


def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    tmpfile = tempfile.TemporaryFile()

    if os.path.exists(file_name):
        r_open = open(file_name, 'r')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open:
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            tmpfile.write(line)
        if not found and append_on_not_exists:
            tmpfile.write('\n' + to_str)
        r_open.close()
        tmpfile.seek(0)

        content = tmpfile.read()

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name, 'w')
        w_open.write(content)
        w_open.close()

        tmpfile.close()
    else:
        print "file %s not found" % file_name

if __name__ == '__main__':
    # 测试

    path="C:\\Config\\global.properties"
    pro = PropertiesUtils(path)

    filedir = pro.get("path")

    print filedir

    filelist = os.listdir(filedir)
    print str(filelist)

    path = "C:\\Users\\Administrator\\PycharmProjects\\GitHub\\PythonDemo\\config\\db.properties"

    pro = PropertiesUtils(path)
    value = pro.get("host")
    print value
    value = pro.get("user")
    print value






