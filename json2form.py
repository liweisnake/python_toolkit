#coding=UTF-8
import json as js
import codecs

with codecs.open("test.json",'r', encoding='UTF-8') as loadf:
    loadcontent = js.load(loadf)
    str = ""
    for item in loadcontent:
        str += item + "=" + loadcontent[item] + "&"
    print(str)