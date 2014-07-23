#!/usr/bin/python
#-*-coding:utf-8-*-
"""(6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．"""
import sys

y = int(sys.argv[2]) #文字を数字化
list = []

for line in open(sys.argv[1]):
	list.insert(0,line.strip())#新しいラインを一番前へ入れていく

for i in range(y):
	print list[i]
