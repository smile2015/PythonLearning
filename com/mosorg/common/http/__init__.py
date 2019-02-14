# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       MyPC
   date：          2019/2/14
-------------------------------------------------
   Change Activity:
                   2019/2/14:
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

if __name__ == '__main__':
    pass