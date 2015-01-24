#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/17 17:03:10 Shin Kanouchi
"""(63) 62の結果を用い，それぞれの名詞句のTF*IDF値を計算し，"(名詞句)\t(TF*IDF値)\t(TF値)\t(DF値)"の形式で出力せよ．
ある名詞句wがあるとき，freq(w)をコーパス全体での名詞句wの出現頻度，df(w)を名詞句wが出現するファイルの数，Nを総ファイル数とし，TF*IDF値は freq(w) * log(N / df(w)) として計算せよ．"""
import re,glob,sys,math
from collections import defaultdict

def make_dict():
	set_list=[]
	all_dict = defaultdict(lambda: 0)
	N=len(glob.glob('62_output_japanese_?.txt'))
	for name in glob.glob('62_output_japanese_?.txt'):
		ward_set =set([])
		for line in open(name):
			ward_set.add(line.strip())
			all_dict[line.strip()] += 1
		set_list.append(ward_set)
	return all_dict,set_list,N

#for word in all_dict.keys():
def make_tf_idf(all_dict,set_list,N):
	for word,ii in sorted(all_dict.items(),key=lambda x:x[1],reverse = True):
		i=0
		for ward_set in set_list:
			if word in ward_set: i+=1
		print '%s\t%.6f\t%d\t%d' % (word,(all_dict[word]*math.log(float(N)/i,2)),all_dict[word],i)

if __name__ == '__main__':
	all_dict,set_list,N=make_dict()
	make_tf_idf(all_dict,set_list,N)