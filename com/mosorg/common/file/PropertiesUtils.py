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
sys.setdefaultencoding('utf8')

'''
自动加载pythonSripts/目录下的properties
'''



class PropertiesUtils:

    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
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

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
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

path="C:\\Config\\global.properties"


pro = parse(path)

filedir = pro.get("path")

print filedir

filelist = os.listdir(filedir)
print str(filelist)

import shutil


'''
#复制单个文件
shutil.copy("C:\\a\\1.txt","C:\\b")
#复制并重命名新文件
shutil.copy("C:\\a\\2.txt","C:\\b\\121.txt")
'''
#复制整个目录(备份)
shutil.copy(filedir,"D:\\notes\\")

'''
#删除文件
os.unlink("C:\\b\\1.txt")
os.unlink("C:\\b\\121.txt")
#删除空文件夹
try:
    os.rmdir("C:\\b\\new_a")
except Exception as ex:
    print("错误信息："+str(ex))#提示：错误信息，目录不是空的
#删除文件夹及内容
shutil.rmtree("C:\\b\\new_a")

#移动文件
shutil.move("C:\\a\\1.txt","C:\\b")
#移动文件夹
shutil.move("C:\\a\\c","C:\\b")

#重命名文件
shutil.move("C:\\a\\2.txt","C:\\a\\new2.txt")
#重命名文件夹
shutil.move("C:\\a\\d","C:\\a\\new_d")
'''
