#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:17:40 Shin Kanouchi

import marshal
list=[]
f1 = open('test32_marshal_dict.txt','rb')

for i in marshal.load(f1):
	 list.append(i)

for line in open('medline4.txt'):
	line = line.strip().split("\t")
	if line[1] in list:
		print (line[1]+" o")
	else:
		print (line[1]+" x")
f1.close()
