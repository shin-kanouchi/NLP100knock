#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:17:40 Shin Kanouchi
"""(33) (32)で作成した辞書を読み込み，１行１単語形式（例えばmedline.txt.sent.tok.stem）で標準入力から読み込んだ単語に対して，辞書引き結果を付与するプログラムを実装せよ．"""
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
		if line[1] in list:
			print (line[1]+" o")
		else:
			print (line[1]+" x")

if __name__ == '__main__':
	list = make_dict()
	main(list)