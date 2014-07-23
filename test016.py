#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:48:01 Shin Kanouchi
"""(16) 括弧表現のうち，括弧の内側がアルファベット大文字の文字列，括弧の左側が漢字の文字列のものを抽出せよ．このとき，括弧の左側の表現と括弧の内側の表現をタブ区切り形式で出力せよ．"""
import re
r = re.compile(r'([一-龥]+)\(([a-zA-Z]+)\)')
for line in open("tweet.txt"):
	if r.search(line):
		print r.search(line).group(1) +"("+ r.search(line).group(2) +")"