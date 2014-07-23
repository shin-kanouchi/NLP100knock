#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 10:48:30 Shin Kanouchi
"""(65) 64のリストに含まれる名詞句に対し，その名詞句に係る文節・その名詞句が係る文節の単語（周辺単語と呼ぶ）を出力するプログラムを実装せよ．周辺単語は名詞，動詞，形容詞の基本形とせよ．出力形式は，"(名詞句)\t(方向) (周辺単語)"とし，名詞句に係る文節では「方向」を"<-"とし，名詞句が係る文節では「方向」を"->"とせよ．以降，「方向」と「周辺単語」を組み合わせたものを，名詞句の「文脈」と呼ぶ．"""
from test054 import *
import re,glob
from collections import defaultdict

def make_words():
	words = []
	for line in open("64_output_tf_idf_top_100.txt"):
		word,tf_idf = line.strip().split(" ")
		words.append(word)
	return words

def test65_morphs(all_sent_list,words):
	import re
	r = re.compile(r"[0-9]")
	for word in words:
		for one_sent_list in all_sent_list:
			for one_chunk in one_sent_list:
				for another_chunk in one_sent_list:
					if one_chunk.num == another_chunk.dst:
						p = one_chunk.main_pos
						p2 = another_chunk.main_pos
						if word in another_chunk.morphs_add and (p == ("名詞" or "動詞" or "形容詞")):
							print (word+"\t->"+one_chunk.main_word)
						if word in one_chunk.morphs_add and (p2 == ("名詞" or "動詞" or "形容詞")):
							print (word+"\t<-"+another_chunk.main_word)

if __name__ == '__main__':
	words = make_words()
	for name in glob.glob('61_output_japanese_?.txt'):
		all_sent_list=test54_morph(name)
		retest65_morphs(all_sent_list,words)
