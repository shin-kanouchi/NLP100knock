#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:37:44 Shin Kanouchi

i = ""
for line in open('medline3.txt'):
	line = line.strip()
	if i != "":
		print (i+'\t'+line)
	i= line