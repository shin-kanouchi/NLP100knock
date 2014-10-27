#!/usr/bin/python
#-*-coding:utf-8-*-
"""(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ．"""
import sys

y = int(sys.argv[2])
list1 = []
for line in open(sys.argv[1]):
	list1.append(line.strip())

for i in range(y):
	print list1[i]
