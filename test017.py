#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 15:11:20 Shin Kanouchi
"""(17) 人名らしき表現にマッチする正規表現を各自で設計し，抽出せよ．（例えば「さん」「氏」「ちゃん」などの接尾辞に着目するとよい）"""
import re
r = re.compile(u'([一-龥ぁ-んァ-ヴ]{1,5})さん')

for line in open("tweet.txt"):
	line = line.decode("utf-8")#decodeしてutf-8にして文字化けを防ぐ
	m = r.search(line)
	if m:
		print m.group(0)