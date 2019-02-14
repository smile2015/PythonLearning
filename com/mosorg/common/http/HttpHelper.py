# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HttpHelper
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

import base64
import urllib
import httplib

class HttpHelper:
    def __init__(self,host, port=80, strict=False, timeout=10):
        self.host=host
        self.port=port
        self.strict=strict
        self.timeout=timeout
        self.headers = None
        self.conn = None
        self.result=None
        self.method=None
        self.url=None
        self.body=None
        self.protocol=0

    def getConnet(self):
        if self.protocol==0:
            self.conn=httplib.HTTPConnection(self.host,self.port,self.strict,self.timeout)
            print "Connet success."
        elif self.protocol==1:
            self.conn = httplib.HTTPConnection(self.host, self.port, self.strict, self.timeout)
            print "Connet success."
        else:
            print "Protocol is unsupport."

    def sendMsg(self,method,url,body=None,headers=None,protocol=0):
        self.protocol=protocol
        self.method=method
        self.url=url
        self.headers=headers
        self.getConnet()
        self.body= body
        self.conn.request(self.method,self.url,self.body,self.headers)
        res=self.conn.getresponse()
        print res.status
        self.result=res.read()
        self.conn.close()

def testdd():
    os = 'xp'
    eth0_ip = '192.168.1.1'

    params = urllib.urlencode({"os": os, "eth0_ip": eth0_ip})
    auth = base64.b64encode('cleartext username' + ':' + 'cleartext passwords')
    headers = {"Authorization": "Basic " + auth}
    conn = httplib.HTTPConnection("10.10.10.10")
    conn.request("POST", "/my/cgi-bin/test.sh", params, headers)
    response = conn.getresponse()
    # print response.status
    print response.read().strip()

def testHttplibDemo():
    headers = {
        'user-agent': 'test'}
    conn = httplib.HTTPConnection('www.baidu.com', 80,False,10)
    conn.request('GET', '/', body=None, headers=headers)
    res = conn.getresponse()
    body = res.read()
    print body
    conn.close()


class HttpRequestGETTest(object):
    def __init__(self):
        # self.body='{"UserName":"Admin","Password":"693aa8d0806c532115637809a863b1a3","sessionID":""}'
        ''''''
        self.headers = {
            "Referer": '192.168.1.1',
            "Accept-Encoding": "gzip, deflate,sdch",
            "Connection": "Keep-Alive",
            'user-agent': 'test'}

        #self.headers = { 'user-agent': 'test'}

    def http_get(self):
        conn = httplib.HTTPConnection(host='www.baidu.com', port=80, strict=True, timeout=10)
        conn.request(method='GET', url='/', body=None, headers=self.headers)
        a = conn.getresponse().read()
        print a
        conn.close()

def getConnet(host,port,strict,timeout,protocol):
    driver=None
    if protocol==0:
        driver=httplib.HTTPConnection(host,port,strict,timeout)
        print "Connet success."
    elif protocol==1:
        driver = httplib.HTTPConnection(host, port, strict, timeout)
        print "Connet success."
    else:
        print "Protocol is unsupport."
    print driver
    return driver

def sendMsg(driver,method,url,body=None,headers=None):
    driver.request(method,url,body,headers)
    res=driver.getresponse()
    print res.status
    result=res.read()
    print result
    driver.close()


if __name__ == '__main__':
    #testHttplibDemo()
    #lianxi = HttpRequestGETTest()
    #lianxi.http_get()
    host='www.baidu.com'
    port = 80
    strict = False
    timeout = 10

    method='GET'
    url='/'
    body=''
    headers={'user-agent':'test'}
    protocol=0

    #conn=getConnet(host, port, strict, timeout, protocol)
    #sendMsg(conn,method,url,body,headers)
    conn3 = httplib.HTTPConnection('www.baidu.com', 80, False, 10)
    conn3.request('GET', '/', '', {'user-agent': 'test'})
    res = conn3.getresponse()
    body = res.read()
    print body
    conn3.close()

