#!/usr/bin/python
#-*-coding:utf-8-*-
"""(3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．"""
import sys

f1,f2= open('col1.txt','w'),open('col2.txt','w')
for line in open(sys.argv[1]):
	(itemList1,itemList2) = line.split('\t').strip()
	f1.write(itemList1+"\n")
	f2.write(itemList2+"\n")
f1.close(),f2.close()
