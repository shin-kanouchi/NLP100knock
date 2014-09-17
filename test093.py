#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)

for item in root.xpath('//sentence[@id= "1"]/dependencies[@type= "basic-dependencies"]/dep/governor[@idx= "4"]'):
	for d in item.getparent().iter('dependent'):
		print d.text
"""
for sent in root.iter('sentence'):
	if 'id' in sent.attrib:
		if sent.attrib['id'] == '1':
			for w in sent.iter('dependencies'):
				if 'type' in w.attrib:
					if w.attrib['type'] == 'basic-dependencies':
						for g in w.iter('governor'):
							if g.attrib['idx'] == '4':
								#print g.text
								for d in g.getparent().iter('dependent'):
									print d.text
"""
