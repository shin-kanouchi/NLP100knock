#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 14:19:32 Shin Kanouchi
"""(45) 文章中の「ＡのＢ」という表現（ＡとＢは名詞の１形態素）をすべて抜き出せ．"""
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import re
item_list = []
for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		item_list.append(item)
		i = len(item_list)-1
		if i>1 and item_list[i-2][1]=="名詞" and item_list[i-1][0]=="の" and item_list[i][1]=="名詞":
			print item_list[i-2][0],item_list[i-1][0], item_list[i][0]