#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:04:59 Shin Kanouchi

import sys
from collections import Counter

dict={}
cnt = Counter()

for line in open('inflection.table.txt'):
	itemList = line.strip().split('|')
	if itemList[0] in dict:
		cnt[itemList[0]] += 1
		itemList[0] = itemList[0] + "(" + str(cnt[itemList[0]]+1) + ")"
	dict[itemList[0]] = (itemList[1], itemList[3],itemList[6])

print dict[sys.argv[1]] #入力を読み取りその辞書を表示
"""
for k, v in sorted(dict.items()):
	print k, v
"""