#!/usr/bin/python
#-*-coding:utf-8-*-
"""(28) 各単語から文字バイグラムを抽出するプログラムを実装せよ．また，(27)と同様の方法で，頻度の高い文字バイグラムトップ100（バイグラムと頻度がソートされたもの）を作成せよ．"""
from test10 import *

def main():
	i = None
	list=[]
	for line in open('medline3.txt'):
		line = line.strip()
		if i is not None:
			list.append(i+' '+line)
		i= line
	return list

if __name__ == '__main__':
	list = main()
	test10_1(list)