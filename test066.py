#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/11 18:04:42 Shin Kanouchi
"""(66) 名詞句xの文脈ベクトルを求めよ．
ただし，出力形式は"(名詞句i)\t(文脈i_1):(値i_1)\t...(文脈i_m):(値i_m)\n"とせよ（ただしmは名詞句iの文脈の種類数）．
文脈ベクトルは長さが1になるように正規化しておくとよい．"""

from collections import defaultdict
import sys, math

def make_dict(open_file):
	for line in open(open_file): #真選組	-> する
		word, bun = line.strip().split("\t") #真選組,-> する
		cnt[word][bun] += 1 #cnt[真選組][-> する] += 1
	return cnt

def make_vector_normalization(cnt, dict_norm):
	for word in cnt.iterkeys(): #word=真選組
		i = 0
		for k,v in cnt[word].items(): #cnt[真選組]
			i += v * v
		dict_norm[word] = math.sqrt(i)
	return dict_norm

def test066(cnt, dict_norm):
	for word in cnt.iterkeys():
		sys.stdout.write(word) #改行空白なしで出力
		for k,v in cnt[word].items():
			sys.stdout.write('\t%s : %f' % (k, (float(v)/dict_norm[word])))
		print ""

if __name__ == '__main__':
	cnt = defaultdict(lambda: defaultdict(int))
	dict_norm = defaultdict(lambda: 0)
	cnt = make_dict("65_output.txt")
	dict_norm = make_vector_normalization(cnt, dict_norm)
	test066(cnt, dict_norm)

