#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 16:26:06 Shin Kanouchi
"""(56) 名詞を含む文節が，動詞を含む文節に係るとき，
これらをタブ区切り形式で抽出せよ．

係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）"""
from test054 import *

def test056(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					s  = one_chunk.morphs_pos("動詞")
					s2 = another_chunk.morphs_pos("名詞")
					if s and s2:
						print '%s\t%s' % (another_chunk.morphs_add, one_chunk.morphs_add)


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	test056(all_sent_list)