#!/usr/bin/python
#-*-coding:utf-8-*-
"""(8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）"""
import sys

def test008_1():
	list1=[]
	for line in open("address0.txt", "r"):
		itemList = line.strip().split('\t')#itemList[0]と[1]を作る
		list1.append(itemList)#listをlistにappend
	return list1

def print_test(list1):
	for w1,w2 in sorted(list1, key=lambda x:x[1]):
			print "%s\t%s" % (w1,w2)

if __name__ == '__main__':
	list1 = test008_1()
	print_test(list1)