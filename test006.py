#!/usr/bin/python
#-*-coding:utf-8-*-
"""(6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．"""
import sys

list = []
for line in open(sys.argv[1]):
	list.insert(0,line.strip())#新しいlineを0番目に

y = int(sys.argv[2])
for i in range(y):
	print list[i]

"""
l = open("address0.txt").readlines()

y = int(sys.argv[1])
for i in range(y):
	ll = l[len(l)-i-1]
	print ll.strip()
"""