#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

f1,f2= open('col1.txt','w'),open('col2.txt','w')
for line in open(sys.argv[1]):
	(itemList1,itemList2) = line.split('\t')
	itemList1,itemList2 = itemList1.strip() , itemList2.strip()
	f1.write(itemList1+"\n")
	f2.write(itemList2+"\n")
f1.close(),f2.close()

"""
import sys
f1= open('col1.txt','w')
f2= open('col2.txt','w')
for line in open(sys.argv[1]):
	itemList = line[:-1].split('\t')
	f1.write(itemList[0]+"\n")
	f2.write(itemList[1]+"\n")
f1.close()
f2.close()
"""

"""
ちょうさん
import sys
address = {}
for line in open(sys.argv[1]):
	address[line.split('\t')[0] + '\n'] = line.split('\t')[1]
	open('col1.txt', 'w').writelines(address.keys())
	open('col2.txt', 'w').writelines(address.values())
"""

