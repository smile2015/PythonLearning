# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     XmlHelper(转载)
   Description :
   Author :       Administrator
   date：          2019/1/15 0015
-------------------------------------------------
   Change Activity:
                   2019/1/15 0015:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


import os
import xml.etree.ElementTree as ET

'''
    在python中，解析XML文件有很多中方法
    本文中要使用的方法是：xml.etree.ElementTree       
'''
#global var
#show log
SHOW_LOG = True
#XML file
XML_PATH = None

def get_root(path):
    '''parse the XML file,and get the tree of the XML file
    finally,return the root element of the tree.
    if the XML file dose not exist,then print the information'''
    if os.path.exists(path):
        if SHOW_LOG:
            print('start to parse the file : [{}]'.format(path))
        tree = ET.parse(path)
        return tree.getroot()
    else:
        print('the path [{}] dose not exist!'.format(path))

def get_element_tag(element):
    '''return the element tag if the element is not None.'''
    if element is not None:
        if SHOW_LOG:
            print('begin to handle the element : [{}]'.format(element))
        return element.tag
    else:
        print('the element is None!')

def get_element_attrib(element):
    '''return the element attrib if the element is not None.'''
    if element is not None:
        if SHOW_LOG:
            print('begin to handle the element : [{}]'.format(element))
        return element.attrib
    else:
        print('the element is None!')

def get_element_text(element):
    '''return the text of the element.'''
    if element is not None:
        return element.text
    else:
        print('the element is None!')

def get_element_children(element):
    '''return the element children if the element is not None.'''
    if element is not None:
        if SHOW_LOG:
            print('begin to handle the element : [{}]'.format(element))
        return [c for c in element]
    else:
        print('the element is None!')

def get_elements_tag(elements):
    '''return the list of tags of element's tag'''
    if elements is not None:
        tags = []
        for e in elements:
            tags.append(e.tag)
        return tags
    else:
        print('the elements is None!')

def get_elements_attrib(elements):
    '''return the list of attribs of element's attrib'''
    if elements is not None:
        attribs = []
        for a in elements:
            attribs.append(a.attrib)
        return attribs
    else:
        print('the elements is None!')

def get_elements_text(elements):
    '''return the dict of element'''
    if elements is not None:
        text = []
        for t in elements:
            text.append(t.text)
        return dict(zip(get_elements_tag(elements), text))
    else:
        print('the elements is None!')

def init():
    global SHOW_LOG
    SHOW_LOG = True
    global XML_PATH
    XML_PATH = 'c:\\test\\hongten.xml'

def main():
    init()
    #root
    root = get_root(XML_PATH)
    root_tag = get_element_tag(root)
    print(root_tag)
    root_attrib = get_element_attrib(root)
    print(root_attrib)
    #children
    children = get_element_children(root)
    print(children)
    children_tags = get_elements_tag(children)
    print(children_tags)
    children_attribs = get_elements_attrib(children)
    print(children_attribs)

    print('#' * 50)
    #获取二级元素的每一个子节点的名称和值
    for c in children:
        c_children = get_element_children(c)
        dict_text = get_elements_text(c_children)
        print(dict_text)

if __name__ == '__main__':
    main()
