#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)

for item in root.xpath('//sentence[@id= "1"]/tokens/token/lemma'):
        print item.text

"""
for sent in root.iter('sentence'):
    if sent.get('id') == '1':
            for w in sent.iter('token'):
                    if 'id' in w.attrib:
                                for x in w.iter('lemma'):
                                        print x.text
"""
