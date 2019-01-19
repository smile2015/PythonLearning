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
import os

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class FileUtils:

    def __init__(self):
        """

        :rtype: object
        """
        self.file=None

    def open_file(self,file_path,mode=None):
        self.file = open(file_path, mode)
        return self.file

    def close_file(self):
        self.file.close()

    def read_lines(self,size=None):
        return self.file.readlines(size)

    def read_line(self,size=None):
        return self.file.readline(size)

    def getCurrentPath(self):
        return os.getcwd()

    def getWorkDir(self):
        return os.path.dirname(os.path.abspath(__file__))

    def getAbsPath(self,offset='.'):
        print os.path.abspath(offset)
        return os.path.abspath(offset)


if __name__ == '__main__':
    # 测试

    file="MySQLHelper.py"

    fileUtil=FileUtils()
    os.path.abspath('..')
    print  fileUtil.getCurrentPath()+"\n"+fileUtil.getAbsPath('..')


    '''
    import shutil



    #复制单个文件
    shutil.copy("C:\\a\\1.txt","C:\\b")
    #复制并重命名新文件
    shutil.copy("C:\\a\\2.txt","C:\\b\\121.txt")
    '''
    # 复制整个目录(备份)
    # shutil.copy(filedir,"D:\\notes\\")

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



