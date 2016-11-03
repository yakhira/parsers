#!/usr/bin/python3

import re
import urllib.request
import urllib.parse

url = 'http://cizincijmk.cz/content/433'

def getRegUrl(url):
    count = -1
    request = urllib.request.urlopen(url)
    expr1 = re.compile('.*<p>A1.1</p>')
    expr2 = re.compile('.*<p><a href="(.*)" target="_blank">REGISTRACE</a></p>') 

    for line in request:
        line = str(line).rstrip()
        if expr1.match(line):
            count = 0
        if count > -1:
            count+=1
        if expr2.match(line):
            search = expr2.search(line)
            if count == 16:
                return search.group(1)
    return 'None'

def getFormValues(regUrl):
    request = urllib.request.urlopen(regUrl)
    return request.read()
        
regUrl = getRegUrl(url)
print(getFormValues(regUrl))