#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/19 10:17:44 Shin Kanouchi
"""(51) 日本語の文章をCaboChaで係り受け解析し，ラティス形式（-f1オプション）の解析結果を得よ．"""
#ターミナル上でこれでも
#shin-no-Air:test kanouchishin$ CaboCha -f1 japanese.txt >cabocha_japanese.txt

import CaboCha
def cabocha_japanese():
	c = CaboCha.Parser()
	for line in open("japanese_tail10.txt"):
		m = c.parseToString(line)
		print m

if __name__ == '__main__':
	cabocha_japanese()