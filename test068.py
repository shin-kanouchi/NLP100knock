#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/17 17:49:25 Shin Kanouchi
"""(68) すべての名詞句のペアに対し，文脈ベクトルの内積が0.6以上のペアをすべて抜きだし，内積値が大きい順に並べよ．このとき，出力形式は"(内積値)\t(名詞句1)\t(名詞句2)\n"とせよ．"""
from collections import defaultdict
from retest67 import *

def retest_68():
	value_dict = defaultdict(lambda: 0)
	word_dict = make_vector("66_output.txt")
	for word1 in word_dict:
		for word2 in word_dict:
			if word1 != word2:
				if word2+" "+word1 not in value_dict:
					value_dict[word1+" "+word2] = calculate_vector(word_dict,word1,word2)
				#print word1,"*",word2,"=",ans
	return value_dict

def sort_dict(value_dict):
	for word,i in sorted(value_dict.items(),key=lambda x:x[1],reverse = True):
		if float(i) >= 0.4:
			print (i+"\t"+word.split()[0]+"\t"+word.split()[1])

if __name__ == '__main__':
	value_dict= retest_68()
	sort_dict(value_dict)
