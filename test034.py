#!/usr/bin/python
#-*-coding:utf-8-*-

import marshal
list=[]

f1 = open('test32_marshal_dict.txt','rb')

for i in marshal.load(f1):
	 list.append(i)

for line in open('medline4.txt'):
	line = line.strip().split("\t")
	if line[1] not in list:
		print line[1]
f1.close()