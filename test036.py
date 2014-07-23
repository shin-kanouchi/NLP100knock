#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:37:44 Shin Kanouchi
"""(36) １行１単語形式（medline.txt.sent.tok）を読み込み，単語の連接を出力するプログラムを実装せよ．ただし，出力形式は"(現在の単語)\t(次の単語)"とせよ．"""

i = ""
for line in open('medline3.txt'):
	line = line.strip()
	if i != "":
		print (i+'\t'+line)
	i= line