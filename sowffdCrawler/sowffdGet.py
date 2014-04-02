# -*- coding: utf-8 -*-
import urllib.request
import json
from bs4 import BeautifulSoup

def JsonData(inputType,inputNumber):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	             'Accept':'text/html;q=0.9,*/*;q=0.8',
	             'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	             'Accept-Encoding':'gzip',
	             'Connection':'close',
	             'Referer':None
	             }
	url = 'http://sowffd.sfaa.gov.tw/CharityFunds/charity_showDetail.detail?id='+ inputType + inputNumber;

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
	'''
	print(thString[0],tdString[0])
	print(thString[1],tdString[1])
	print(thString[2],tdString[2])
	print(thString[3],tdString[3])
	print(thString[4],tdString[4])
	print(thString[5],tdString[5])
	print(thString[6],tdString[6],tdString[7])
	print(thString[7],tdString[8],tdString[9])
	print(thString[8],tdString[10])
	print(thString[9],tdString[11])
	print(thString[10],tdString[12])
	'''
	data = [{thString[0]:tdString[0], #JSON 結構
			thString[1]:tdString[1],
			thString[2]:tdString[2],
			thString[3]:tdString[3],
			thString[4]:tdString[4],
			thString[5]:tdString[5],
			thString[6]:[
				{
					"0":tdString[6]
				},{
					"1":tdString[7]
				}],
			thString[7]:[
				{
					"0":tdString[8]
				},{
					"1":tdString[9]
				}
				],
			thString[8]:tdString[10],
			thString[9]:tdString[11],
			thString[10]:tdString[12]
			}
			]
	data_string = json.dumps(data, ensure_ascii=False, indent=2)
	#print ("JSON:",data_string)
	file = open("data.json","a+",encoding="utf-8")
	file.write(data_string)
	file.close()

if __name__ == "__main__":
	maxCount = 300 #網址規則判斷
	count = 1
	inputType = 0
	typeList=['A','B','C','D','E','F']

	while (inputType<=5):
		while (count<=maxCount):
			if(count//100>=1):
				print(typeList[inputType],inputNumber)
				inputNumber = '0' + str(count)
				JsonData(typeList[inputType],str(inputNumber))
				count += 1
			else:
				if(count//10>=1):
					inputNumber = '00' + str(count)
					print(typeList[inputType],inputNumber)
					JsonData(typeList[inputType],inputNumber)
					count += 1
				else:
					inputNumber = '000' + str(count)
					print(typeList[inputType],inputNumber)
					JsonData(typeList[inputType],inputNumber)
					count += 1
		inputType+=1
		count=1

	import jsonAdjust
