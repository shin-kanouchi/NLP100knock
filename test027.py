#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:24:21 Shin Kanouchi
"""(27) (10)のプログラムを呼び出すことで，頻度の高い英単語トップ100（単語と頻度がソートされたもの）を作成せよ．"""
from test010 import *

def main():
	list=[]
	for line in open('medline3.txt'):
		list.append(line.strip())
	return list

if __name__ == '__main__':
	list = main()
	test10_1(list)