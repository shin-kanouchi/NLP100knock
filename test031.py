#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:04:59 Shin Kanouchi
"""(31) このファイルを読み込み，単語をキーとして，品詞，活用形，基本形のタプルのリストを値とするマッピング型に格納せよ．プログラムの動作を確認するため，標準入力から読み込んだ単語の語彙項目を閲覧するプログラムを実装せよ．"""
import sys
from collections import Counter

def main():
	cnt = Counter()
	dict={}
	for line in open('inflection.table.txt'):
		itemList = line.strip().split('|')
		if itemList[0] in dict:
			cnt[itemList[0]] += 1
			itemList[0] = itemList[0] + "(" + str(cnt[itemList[0]]+1) + ")"
		dict[itemList[0]] = (itemList[1], itemList[3],itemList[6])

if __name__ == '__main__':
	dict = main()
	print dict[sys.argv[1]] #入力を読み取りその辞書を表示

	"""全部表示する
	for k, v in sorted(dict.items()):
		print k, v
	"""