#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57 Shin Kanouchi
"""(57) (56)を修正し，非自立語は出力に含めないようにせよ．
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）"""
from test054 import *

def test057(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					s  = one_chunk.morphs_pos("動詞")
					s2 = one_chunk.morphs_pos1("非自立")
					s3 = another_chunk.morphs_pos("名詞")
					s4 = another_chunk.morphs_pos1("非自立")
					if s and s2 == False and s3 and s4 == False:
						print '%s\t%s' % (another_chunk.morphs_add, one_chunk.morphs_add)


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	test057(all_sent_list)