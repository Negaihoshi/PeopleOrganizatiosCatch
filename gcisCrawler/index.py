# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

def indexPaser(name):

    file = open(name, 'r', encoding='UTF-8')
    fileData = file.read()

    list, dataStruct = [], {}
    dataStruct = {
        "編號": "",
        "分類": "",
        "名稱": "",
    }

    for line in fileData.split('\n'):
        try:
            dataSplit = line.split(',')
            dataStruct['編號'] = dataSplit[0]
            dataStruct['分類'] = dataSplit[1]
            dataStruct['名稱'] = dataSplit[2]
            print(dataStruct['編號'],dataStruct['分類'])

            if dataStruct['分類'] == '公司':
                companyfile = open('company.txt', 'a+', encoding='UTF-8')
                companyfile.write(line+'\n')
                companyfile.close()
            elif dataStruct['分類'] == '商業登記':
                businessfile = open('business.txt', 'a+', encoding='UTF-8')
                businessfile.write(line+'\n')
                businessfile.close()

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



if __name__ == "__main__":
    filename = 'index.csv'
    indexPaser(filename)


