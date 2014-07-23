#!/usr/bin/python
#-*-coding:utf-8-*-
"""(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．"""
import sys
list = []

for line in open(sys.argv[1]):
	itemList = line[:-1].split('\t')
	list.append(itemList[0])

print ("単語数 "+ str(len(list)))
print ("ことなり数 "+str(len(set(list))))
