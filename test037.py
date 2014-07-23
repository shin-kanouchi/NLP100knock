#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:42:20 Shin Kanouchi

from collections import Counter
list=[]
for line in open('retest36.txt'):
	list.append(line.strip())

counter = Counter(list)

for word, cnt in sorted(counter.most_common(),key=lambda x:x[1],reverse = True):
	print (str(cnt)+"\t"+word)
