#!/usr/bin/python
#-*-coding:utf-8-*-
"""(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．"""
import sys

list1 = []
for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	list1.append(itemList[0])

print "単語数:", len(list1)
print "ことなり数: ", len(set(list1))