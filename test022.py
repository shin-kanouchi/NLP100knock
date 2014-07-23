#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:07:16
"""(22) (21)のプログラムは破棄して，標準入力から英語のテキストを読み込み，ピリオド→スペース→大文字を文の区切りと見なし，１行１文の形式で標準出力に書き出せ"""
import  re
re_sentence = re.compile(r"(\.) ([A-Z])")

for line in open('medline.txt'):
	m = re_sentence.split(line.strip())

m = [m[0][0], m[0][1:]] + m[1:-1] + [m[-1][0:len(m[-1])-1], m[-1][-1]]

for i in range(0, len(m)-1, 3):
	print m[i]+m[i+1]+m[i+2]