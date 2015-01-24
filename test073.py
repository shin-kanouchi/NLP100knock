#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/27 14:57:04 Shin Kanouchi
"""(73) 72のモジュールを用い，名詞句（NP）を抽出するプログラムを実装せよ．
ただし，ひとつの名詞句の出現に対し，"# (名詞句)\n"という形式で出力せよ．"""
from test072 import *

def test073(all_sent_list):
	for one_sent_list in all_sent_list:
		w = ''
		for one_chunk in one_sent_list:
			if one_chunk.chunk == "B-NP":
				if w.startswith('#'):
					print w
				w = '# ' + one_chunk.surface
			elif one_chunk.chunk == "I-NP" and w !='':
				w = w + ' ' + one_chunk.surface
			elif w != '':
				print w
				w = ''
			else: 
				pass

if __name__ == '__main__':
	for name in glob.glob('71_GENIA_tagger_?.txt'):
		all_sent_list = test072(name)
		test073(all_sent_list)