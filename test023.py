#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:10:55
"""１行１文形式のテキストmedline.txt.sentを，１行１単語形式のテキストmedline.txt.sent.tokに変換するプログラムを次のように実装せよ．
(23) (22)の出力を標準入力から１行（１文）を読み込む毎に，スペースで単語列に分割し，１行１単語形式で標準出力に書き出せ．文の終端を表すため，文が終わる毎に空行を出力せよ．"""
for line in open('medline2.txt'):
	itemList = line.strip().split(' ')

	for w in itemList:
		w = w.replace('.','\n')
		print w