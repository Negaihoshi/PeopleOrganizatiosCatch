# -*- coding: utf-8 -*-
import json
import re

file=open("data.json","r",encoding="utf-8")
file2=open("data2.json","w",encoding="utf-8")
file_str=file.read()
#result=re.findall("\]\[", file_str)
#re.sub(r"(\w)(\w+)(\w)", repl, file_str)
result=re.sub("\]\[",",",file_str)
file2.write(result)
file.close()
file2.close()
