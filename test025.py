#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:17:29 Shin Kanouchi
"""
(25) (24)の出力を標準入力から１行（１単語）を読み込む毎に，その単語を小文字に変換した文字列を各行の最終列にタブ区切り形式で追加し，標準出力に書き出せ．"""
for line in open('medline3.txt'):
	itemList = line.strip().lower()

	print (line.strip() +"\t"+ itemList)