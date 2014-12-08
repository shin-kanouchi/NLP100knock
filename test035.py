#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:40:29 Shin Kanouchi
"""(35) 辞書引きを行った結果，３つ以上のエントリが見つかったもののみを出力せよ．"""
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
		line2 = line[1] + "(3)"
		if line2 in list:
			print (line[1]+" 3~")

if __name__ == '__main__':
	list = make_dict()
	main(list)