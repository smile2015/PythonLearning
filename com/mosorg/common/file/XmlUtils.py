# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     XmlUtils
   Description :
   Author :       Administrator
   date：          2019/1/14 0014
-------------------------------------------------
   Change Activity:
                   2019/1/14 0014:
-------------------------------------------------
"""
from com.mosorg.common.file.FileUtils import FileUtils

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class XmlUtils:

    def __init__(self):
        self.values=[]
        self.fileUtils=FileUtils()

    ##
    # 加载xml
    #
    # @param file_path
    def loadXml(self,file_path):
        # 解析文件
        self.tree = ET.parse(file_path)
        # 获得根节点
        self.root = self.tree.getroot()

    ##
    # Get node by tag name
    #
    # @param elmentNode
    # @param tagName
    def getNodeByTagName(self,elmentNode,tagName):
        # 找到第一个tagName标签
        return elmentNode.find(tagName)

    ##
    # Get node attr value
    #
    # @param elementNode
    # @param attrName
    def getNodeAttrValue(self,elementNode,attrName):
        # 获得属性
        attrValue=elementNode.get(attrName)
        print attrValue
        return attrValue

    ##
    # Get nodes by tag name
    #
    # @param tagName
    def getNodesByTagName(self,tagName,elmenetNode=None):
        # 遍历所有的tagName标签
        if None == elmenetNode:
            return self.root.findall(tagName)
        else:
            return elmenetNode.findall(tagName)

    ##
    # Get node by tag name
    #
    # @param tagName
    def getNodeByTagName(self, elmenetNode, tagName):
        return elmenetNode.find(tagName)


    ##
    # Get node value by tag name
    #
    # @param elementNode
    # @param tagName
    def getNodeValuesByTagName(self,elementNode,tagName):
        # 遍历所有的tagName标签
        for ele in elementNode.findall(tagName):
            value=ele.text
            print value
            self.values.append(value)
        return self.values


    ##
    # Get node text
    #
    # @param elementNode
    def getText(self,elementNode):
        return elementNode.text


    ##
    # Create root node
    #
    # @param nodeName
    def createRootNode(self,nodeName):
        return ET.Element(nodeName)

    ##
    # Create child element
    #
    # @param parentNode
    # @param childNodeName
    def createSubElement(self,parentNode,childNodeName):
        return ET.SubElement(parentNode, childNodeName)

    ##
    # Set attr for element
    #
    # @param elementNode
    # @param attrName
    # @param attrValue
    def setNodeAttr(self,elementNode,attrName,attrValue):
        # 修改或新建属性
        elementNode.set(attrName, attrValue)
        return True

    ##
    # Set value for element
    #
    # @param elementNode
    # @param value
    def setText(self,elementNode,value):
        elementNode.text = value

    ##
    # Create new XML
    #
    # @param rootNode
    def createNewXml(self,rootNode):
        self.indent(rootNode)
        self.tree = ET.ElementTree(rootNode)

    ##
    # Save a xml
    #
    # @param file_path
    # @param mode .
    # @param encoding
    def saveXml(self,file_path,mode="w",encoding="utf-8"):
        fopen=self.fileUtils.open_file(file_path,mode)
        #xml_declaration=True  --指定xml头。如：<?xml version='1.0' encoding='utf-8'?>
        self.tree.write(fopen, encoding, xml_declaration=True)
        self.fileUtils.close_file()

    ##
    # 格式化XML
    #
    # @param rootNode
    # @param level .
    def indent(self,rootNode, level=0):
        i = "\n" + level * "\t"
        if len(rootNode):
            if not rootNode.text or not rootNode.text.strip():
                rootNode.text = i + "\t"
            if not rootNode.tail or not rootNode.tail.strip():
                rootNode.tail = i
            for elem in rootNode:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not rootNode.tail or not rootNode.tail.strip()):
                rootNode.tail = i


