#!/usr/bin/python
#-*-coding:utf-8-*-
"""(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．"""
import sys

def test10_1(list):
	from collections import Counter
	counter = Counter(list)
	for word, cnt in sorted(counter.most_common(),key=lambda x:x[1],reverse = True):
		print word, cnt

if __name__ == '__main__':
	list=[]
	for line in open("col2.txt", "r"):
		list.append(line.strip())
	test10_1(list)