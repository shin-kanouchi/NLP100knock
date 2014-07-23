#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/27 15:35:26 Shin Kanouchi
"""(74) 73で作成したプログラムを改変し，名詞句の冠詞が不定冠詞の場合は"A"，定冠詞の場合は"THE"，無冠詞の場合は"NONE"と表示するプログラムを実装せよ．ただし，73の表示内容に追加し，"# (名詞句)\n(冠詞タイプ)\n"という出力形式にせよ．"""
from test072 import *
def make_kansi(w):
	item = w.split()
	l = item[1].lower()
	if l == ('a' or 'an'):
		w = w + '\n' + 'A'
	elif l == 'the':
		w = w + '\n' + 'THE'
	else:
		w = w + '\n' + 'NONE'
	return w

def test74(all_sent_list):
	for one_sent_list in all_sent_list:
		w = ''
		for one_chunk in one_sent_list:
			if one_chunk.chunk == "B-NP":
				if w.startswith('#'):
					w = make_kansi(w)
					print w
				w = '# ' + one_chunk.surface
			elif one_chunk.chunk == "I-NP" and w !='':
				w = w +' '+ one_chunk.surface
			elif w !='':
				w = make_kansi(w)
				print w
				w=''
			else: pass

if __name__ == '__main__':
	for name in glob.glob('71_GENIA_tagger_?.txt'):
		all_sent_list=test72(name)
		test74(all_sent_list)
