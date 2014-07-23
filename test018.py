#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 15:29:21 Shin Kanouchi
"""(18) 仙台市の住所らしき表現にマッチする正規表現を各自で設計し，抽出せよ．"""
import re
r = re.compile(u'([一-龥]{1,5}市)')

for line in open("tweet.txt"):
	m = r.search(line.decode("utf-8"))
	if m :
		print m.group(0)
