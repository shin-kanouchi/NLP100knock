#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:14:33 Shin Kanouchi
"""(32) (31)で読み込んだマッピング型オブジェクトを，marshalモジュールを使ってファイルに書き出せ．書き出したファイルを今後「辞書」と呼ぶ．"""
import marshal
from collections import Counter

def main():
	dict={}
	cnt = Counter()
	f1 = open('test032_Mdict.txt','wb')
	for line in open('inflection.table.txt'):
		itemList = line.strip().split('|')
		if itemList[0] in dict:
			cnt[itemList[0]] += 1
			itemList[0] = itemList[0] + "(" + str(cnt[itemList[0]]+1) + ")"
		dict[itemList[0]] = (itemList[1], itemList[3], itemList[6])
	marshal.dump(dict, f1)
	f1.close()

if __name__ == '__main__':
	main()