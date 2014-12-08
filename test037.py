#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:42:20 Shin Kanouchi
"""(37) (36)の出力を読み込み，単語の連接の頻度を求めよ．ただし，出力形式は"(連接の頻度)\t(現在の単語)\t(次の単語)"とせよ．"""

from collections import Counter

def count_():
	list=[]
	for line in open('test036.txt'):
		list.append(line.strip())
	counter = Counter(list)
	return counter

def main(counter):
	for word, cnt in sorted(counter.most_common(),key=lambda x:x[1],reverse = True):
		print (str(cnt)+"\t"+word)

if __name__ == '__main__':
	counter = count_()
	main(counter)