#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)

for item in root.xpath('//sentence[@id= "2"]/tokens/token[@id= "5"]/word'):
        print item.text
"""
for sent in root.iter('sentence'):
	if sent.get('id') == '2':
		for w in sent.iter('token'):
			if w.get('id') == '5':
				for x in w.iter('word'):
					print x.text
"""

