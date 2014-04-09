#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: rtseng
# @Date:   2014-03-12 14:14:13
# @Last Modified by:   rtseng
# @Last Modified time: 2014-04-09 15:42:28

import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import umsgpack

dataStruct = { "編號": id,
    "編號": "",
    "分類": "",
    "名稱": "",
}
def filePaser(fileData):
    for line in fileData.split('\n'):
        try:
            dataSplit = line.split(',')
            dataStruct['編號'] = dataSplit[0]
            dataStruct['分類'] = dataSplit[1]
            dataStruct['名稱'] = dataSplit[2]
            #print(dataStruct['編號'],dataStruct['分類'],dataStruct['名稱'])

            if dataStruct['分類'] == '公司':
                companyfile = open('companyData.txt', 'a+', encoding='UTF-8')
                JsonData = WebRequest(apiSite + dataStruct['編號'])
                companyfile.write(str(umsgpack.packb(JsonData)) + '\n')
                companyfile.close()
            elif dataStruct['分類'] == '商業登記':
                businessfile = open('businessData.txt', 'a+', encoding='UTF-8')
                JsonData = WebRequest(apiSite + dataStruct['編號'])
                businessfile.write(str(umsgpack.packb(JsonData)) + '\n')
                businessfile.close()
            else:
                subCompanyfile = open('subCompanyData.txt', 'a+', encoding='UTF-8')
                JsonData = WebRequest(apiSite + dataStruct['編號'])
                subCompanyfile.write(str(umsgpack.packb(JsonData)) + '\n')
                subCompanyfile.close()

        except IndexError as e:
            print (e)
            print(line)
        except UnicodeEncodeError as e:
            print (e)
        except AttributeError as e:
            print (e)
            print(line)
            errorFile = open("error.json","a+",encoding="utf-8")
            errorFile.write(line+'\n')
            errorFile.close()

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
    return req.json()
    #print (req.json())

def FileRead(name):
    file = open(name, 'r', encoding='UTF-8')
    return file.read()

if __name__ == "__main__":
    #JsonData(str(243368320))
    #WebRequest('http://company.g0v.ronny.tw/api/show/'+'97751885')
    apiSite = 'http://company.g0v.ronny.tw/api/show/'

    filePaser(FileRead('company.txt'))
    filePaser(FileRead('business.txt'))
    filePaser(FileRead('subcompany.txt'))