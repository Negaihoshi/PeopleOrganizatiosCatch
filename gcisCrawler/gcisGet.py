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
	payload = {
		'Host':'gcis.nat.gov.tw',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-tw,zh;q=0.8,en-us;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Connection':'keep-alive',
		'Referer':'http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do'
	}
	getValue = {'method':'detail','banNo':'53670957'}
	headers = {'content-type': 'application/json'}

	req = requests.get(url, data=json.dumps(payload), headers=headers, params=getValue)
	print(req.url)
	print(req.headers)
	req.encoding = 'big5'
	print(req.text)

if __name__ == "__main__":
	#JsonData(str(243368320))
	WebRequest('http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoAction.do')