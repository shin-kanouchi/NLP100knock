#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/05 18:15:45 Shin Kanouchi

"""(54) 以降のプログラムを実装しやすくするため，
(53)のプログラムをモジュール化せよ．"""

from collections import defaultdict
import re

"""
* 23 24D 0/1 1.373627
機関	名詞,一般,*,*,*,*,機関,キカン,キカン
に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
* 24 25D 1/2 0.697440
成長	名詞,サ変接続,*,*,*,*,成長,セイチョウ,セイチョー
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
EOS
"""

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1


class Chunk:
	def __init__(self, num, morphs, morphs_add, dst, srcs,main_word,main_pos):
		self.num        = num
		self.morphs     = morphs
		self.morphs_add = morphs_add
		self.dst        = dst
		self.srcs       = srcs
		self.main_word  = main_word
		self.main_pos   = main_pos

	def morphs_pos(self,w):
		for morphs in self.morphs:
			if morphs.pos == w:
				return True
		return False

	def morphs_pos1(self,w):
		for morphs in self.morphs:
			if morphs.pos1 == w:
				return True
		return False

	def morphs_not_kigo(self):
		w = ""
		for morphs in self.morphs:
			if morphs.pos != "記号":
				w = w + morphs.surface
		return w

	def morphs_base_return(self):
		for morphs in self.morphs:
			if morphs.pos == "名詞" or morphs.pos == "動詞" or  morphs.pos == "形容詞":
				if morphs.base != "*":
					return morphs.base
				else:
					return morphs.surface
		return False


def test054_morph(open_file):
	kakari_dict   = defaultdict(list)
	one_sent      = []
	all_sent_list = []
	for line in open(open_file):
		if "* " in line:
			w         = re.split(r" |/", line.strip())
			w[2]      = w[2][:-1]
			one_chunk = Chunk(w[1], [], "", w[2], [], "", "")
			kakari_dict[w[2]].append(w[1])
			one_sent.append(one_chunk)
			i = 0
		elif "\t" in line:
			item = re.split(r"\t|,", line.strip())
			one_chunk.morphs.append(Morph(item[0], item[7], item[1], item[2]))
			if item[1] != "記号":
				one_chunk.morphs_add = one_chunk.morphs_add + item[0]
			if i == int(w[3]):
				if item[7]== "*":
					item[7] = item[0]
				one_chunk.main_word = item[7]
				one_chunk.main_pos = item[1]
			i+=1
		elif "EOS" in line:
			for one_chunk in one_sent:
				one_chunk.srcs = kakari_dict[one_chunk.num]
			all_sent_list.append(one_sent)
			one_sent = []
			kakari_dict = defaultdict(list)
	return all_sent_list


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")

