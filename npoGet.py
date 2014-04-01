#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: rtseng
# @Date:   2014-03-12 14:14:13
# @Last Modified by:   rtseng
# @Last Modified time: 2014-03-12 16:03:32

import urllib.request
import json
from bs4 import BeautifulSoup

def JsonData(inputNumber):
	'''
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language':'zh-tw,zh;q=0.8,en-us;q=0.5,en;q=0.3';
				'Accept-Encoding':'gzip, deflate',
				'Connection':'keep-alive',
				'Referer':http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do
			}
	'''
	url = 'http://www.npo.org.tw/npolist_detail.asp?id=' + inputNumber;

	print(url)
	try : webpage = urllib.request.urlopen(url)

	except urllib.error.HTTPError as e:
		return None


	soup = BeautifulSoup(webpage.read().decode("utf8"))

	webtext = soup.get_text().strip().split()

	#print(soup.body.table.caption.string) #印出網頁標題

	thString = []
	tdString = []

	for th in soup.find_all('th'):
		thString.append(th.string)
	for	td in soup.find_all('td'):
		tdString.append(td.string)

	data = [{thString[0]:tdString[0], #JSON 結構
			thString[1]:tdString[1],
			thString[2]:tdString[2],
			thString[3]:tdString[3],
			thString[4]:tdString[4],
			thString[5]:tdString[5],
			thString[6]:tdString[6],
			thString[7]:tdString[7],
			thString[8]:tdString[8]
			}
			]
	data_string = json.dumps(data, ensure_ascii=False, indent=2)
	#print ("JSON:",data_string)
	file = open("data.json","a+",encoding="utf-8")
	file.write(data_string)
	file.close()

maxCount = 7000 #網址規則判斷
count = 1


while (count <= maxCount):
	print(count)
	JsonData(str(count).zfill(4))
	count += 1
