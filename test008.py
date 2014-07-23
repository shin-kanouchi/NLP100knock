#!/usr/bin/python
#-*-coding:utf-8-*-
"""(8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）"""
import sys

def retest8_1():
	list=[]
	for line in open("address0.txt", "r"):
		itemList = line.strip().split('\t')#itemList[0]と[1]を作る
		list.append(itemList)#listをlistにappend
	return list

if __name__ == '__main__':
	list2 = retest8_1()
	list2.sort(key=lambda x:x[1])#[1]の要素で並び替え
	for i in range(len(list2)):
			print list2[i][0]+"\t"+list2[i][1]

