#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:57:17
"""(29) stemming 1.0（Porterのステマー）を各自の環境にインストールし，正しくインストールされているか確認せよ．
(30) (25)の出力を標準入力から読み込み，stemming.porter2を用いて語幹（ステム）を最終列に追加し，medline.txt.sent.tok.stemというファイルに保存せよ．"""
from stemming.porter2 import stem

for line in open("medline4.txt"):
	line2 = line.strip().split("\t")
	print (line2[0]+"\t"+line2[1]+"\t"+stem(line2[1]))
