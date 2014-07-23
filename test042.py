#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 14:19:32 Shin Kanouchi
"""(42) 文章中に出現するすべての動詞を抜き出せ．"""
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import re
for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		if item[1] == "動詞":
			print item[0]
