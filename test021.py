#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:01:10 Shin Kanouchi
"""英語のテキストmedline.txtを，１行１文形式のテキストmedline.txt.sentに変換するプログラムを，次のように実装せよ．
(21) 標準入力から英語のテキストを読み込み，ピリオドを文の区切りと見なし，１行１文の形式で標準出力に書き出せ．"""

for line in open('medline.txt'):
	itemList1 = line.strip().split('.')
	for w in itemList1:
		print (w + ".")