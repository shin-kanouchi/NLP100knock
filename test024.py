#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:15:05 Shin Kanouchi
"""(24) (23)のプログラムを修正し，各トークンの末尾が記号で終わる場合は，その記号を別のトークンとして分離せよ．"""
import re

r = re.compile(r'(\.$|\,$|\. |\, )')
for line in open('medline2.txt'):
	itemList = r.split(line.strip())
	while ' ' in itemList: itemList.remove(' ')#空白のリストを消す
	for w in itemList:
		print w