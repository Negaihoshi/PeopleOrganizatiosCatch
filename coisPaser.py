#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: rtseng
# @Date:   2014-03-17 17:41:40
# @Last Modified by:   rtseng
# @Last Modified time: 2014-04-01 12:05:51
import json
import re

data =""

def parse_group(plain):
	list, dataStruct = [], {}
	for line in plain.split('\n'):
		try:
			if (re.match('^\s*[0-9]+\s*$', line)):
				if dataStruct != {}: list.append(dataStruct)
				id = re.match('^\s*([0-9]+)\s*$', line).groups()[0]
				dataStruct = { "編號": id,
						"團體名稱": "",
						"團體分類": "",
						"團體細分類": "",
						"理事長": "",
						"稱謂": "",
						"成立日期": "",
						"電話": "",
						"核准立案字號": "",
						"會址": ""
					}
			elif(re.match('^團體名稱.*$', line)):
				dataStruct['團體名稱'] = re.match('^團體名稱\s+([^\s]+)\s*$', line).groups()[0]

			elif(re.match('^團體分類.*$', line)):
				result = re.match('^團體分類\s+([^\s]+)\s*([^\s]+)\s*理事長\s+([^\s]+)\s*([^\s]+)\s*$', line).groups()
				dataStruct['團體分類'] = result[0]
				dataStruct['團體細分類'] = result[1]
				dataStruct['理事長'] = result[2]
				dataStruct['稱謂'] = result[3]

			elif(re.match('^成立日期.*$', line)):
				result = re.match('^成立日期\s+([^\s]+)\s*電話\s*([^\s]+)\s*$', line).groups()
				dataStruct['成立日期'] = result[0]
				dataStruct['電話'] = result[1]

			elif(re.match('^核准立案字號.*$', line)):
				dataStruct['核准立案字號'] = re.match('^核准立案字號\s*([^\s]*)\s*$', line).groups()[0]

			elif(re.match('^會址.*$', line)):
				dataStruct['會址'] = re.match('^會址\s+([^\s]*)\s*$', line).groups()[0]
				#data_string = json.dumps(data, ensure_ascii=False, indent=2)
			else:
				continue
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
	list.append(dataStruct)
	return list

if __name__ == "__main__":
	name = 'TestData.txt'
	file = open(name, 'r', encoding='UTF-8')
	fileData = file.read()
	list = parse_group(fileData)

	toJson = json.dumps(list, ensure_ascii=False, indent=2)
	jsonFile = open("data.json","w+",encoding="utf-8")
	jsonFile.write(toJson)
	jsonFile.close()

	'''
	for dataStruct in list:
		print (["編號"])
		for k, v in dataStruct.items():
			print ("\t", k, v)
	'''

