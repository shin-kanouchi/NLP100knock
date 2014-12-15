#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/06 12:06:12 Shin Kanouchi
"""(59) 各文に含まれるすべての体言（名詞を含む文節）の組み合わせに対し，
その文節間の表現（係り受けパス）を出力せよ．"""

from test054 import *

def test059(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					s  = one_chunk.morphs_pos("名詞")
					s2 = another_chunk.morphs_pos("名詞")
					if s and s2 :
						print another_chunk.morphs_add,one_chunk.morphs_add
						print another_chunk.num,"->",one_chunk.num

if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	test059(all_sent_list)