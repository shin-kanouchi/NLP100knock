#!/usr/bin/python
#-*-coding:utf-8-*-
"""(34) 辞書引きを行った結果，辞書に載っていなかった語のみを出力せよ．"""

import marshal

def make_dict():
	list=[]
	f1 = open('test032_Mdict.txt','rb')
	for i in marshal.load(f1):
		 list.append(i)
	return list

def main(list):
	for line in open('medline4.txt'):
		line = line.strip().split("\t")
		if line[1] not in list:
			print line[1]

if __name__ == '__main__':
	list = make_dict()
	main(list)