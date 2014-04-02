#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: rtseng
# @Date:   2014-03-12 14:14:13
# @Last Modified by:   rtseng
# @Last Modified time: 2014-03-17 15:49:09

import urllib.request
import json
from bs4 import BeautifulSoup
import requests

def BSPaser(req):
    print(req)
    soup = BeautifulSoup(req.read().decode("utf8"))

    webtext = soup.get_text().strip().split()

    print(soup.head.title)
    print(webtext)


def WebRequest(url):

    req = requests.get(url)
    print(req.url)
    req.encoding
    print (req.json())

if __name__ == "__main__":
    #JsonData(str(243368320))

    WebRequest('http://company.g0v.ronny.tw/api/show/'+'00000607')