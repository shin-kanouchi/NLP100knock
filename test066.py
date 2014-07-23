#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/11 18:04:42 Shin Kanouchi
"""(66) 名詞句xの文脈ベクトルを求めよ．ただし，出力形式は"(名詞句i)\t(文脈i_1):(値i_1)\t...(文脈i_m):(値i_m)\n"とせよ（ただしmは名詞句iの文脈の種類数）．文脈ベクトルは長さが1になるように正規化しておくとよい．"""

from collections import defaultdict
import sys,math

def make_dict(open_file):
	for line in open(open_file):#真選組	-> する
		word,bun= line.strip().split("\t")#真選組,-> する
		cnt[word][bun] += 1 #cnt[真選組][-> する] += 1

def make_vector_normalization():
	for word in cnt.keys():#word=真選組
		ii=0
		for k,v in cnt[word].items():#cnt[真選組]
			ii += v*v
		dict_norm[word] = math.sqrt(ii)

def test_66():
	for word in cnt.keys():
		sys.stdout.write(word)#改行とか空白なしで出力
		for k,v in cnt[word].items():
			sys.stdout.write("\t"+k+" : "+str(float(v)/dict_norm[word]))
		print ""

if __name__ == '__main__':
	cnt = defaultdict(lambda: defaultdict(int))
	dict_norm = defaultdict(lambda: 0)
	make_dict("65_output.txt")
	make_vector_normalization()
	test_66()

