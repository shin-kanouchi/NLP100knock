#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:34:54 Shin Kanouchi
"""(58) 係り元が２つ以上ある文節に対し，その文節とすべての係り元を表示せよ．"""
from test054 import *

def test58_morph(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			if len(one_chunk.srcs) > 1:
				for another_chunk in one_sent_list:
					if one_chunk.num == another_chunk.dst:
						print another_chunk.morphs_add,one_chunk.morphs_add

if __name__ == '__main__':
	all_sent_list=test54_morph("cabocha_japanese.txt")
	test58_morph(all_sent_list)
