#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 17:41:19 Shin Kanouchi
"""(46) 文章中のすべての名詞の連接（１形態素以上）を抜き出せ．"""
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import re
list_meisi=[]
for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		if item[1] == "名詞":
			list_meisi.append(item[0])
		elif len(list_meisi) > 1:
			for meisi in list_meisi:
				print meisi,
			print ""
			list_meisi=[]
		else:
			list_meisi=[]