#!/usr/bin/python
#-*-coding:utf-8-*-
"""(6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．"""
import sys

y = int(sys.argv[1]) #文字を数字化

l = open("address0.txt").readlines()

for i in range(y):
	ll = l[len(l)-i-1]
	print ll.strip()
