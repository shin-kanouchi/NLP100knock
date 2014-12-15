#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 16:29:03 Shin Kanouchi
"""(55) 係り元の文節と係り先の文節をタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．

係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）"""
from test054 import *

def test055(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					print '%s\t%s' % (another_chunk.morphs_add, one_chunk.morphs_add)


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	test055(all_sent_list)
