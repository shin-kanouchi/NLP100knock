#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 14:11:14 Shin Kanouchi
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
one_sent = []
import re
for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() == "EOS":
		continue
	item = re.split(r"\t|,",line.strip())
	dict = {'surface':item[0], 'base' : item[7] ,'pos':item[1],'pos1':item[2]}
	one_sent.append(dict)

for d in one_sent:
	for k,w in d.items():
		print k,w,
	print ""