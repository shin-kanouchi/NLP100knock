#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/27 14:39:54 Shin Kanouchi
"""(72) 71の解析結果を読み込むモジュールを実装せよ．各トークンは表層形（w），レンマ（lem），品詞（pos），チャンクタグ（chunk）をキーとするマッピング型に格納し，１文はトークン（マッピング型）のリストとして表現せよ（固有表現情報は読み込まなくてもよい）．"""
from collections import defaultdict
import glob

class Morph:
	def __init__(self, surface, lem, pos, chunk):
		self.surface = surface
		self.lem = lem
		self.pos = pos
		self.chunk = chunk

def test72(name):
	one_sent_list = []
	all_sent_list = []
	for line in open(name):
		if "\t" in line:
			item = line.strip().split("\t")
			one_sent_list.append(Morph(item[0],item[1],item[2],item[3]))
		else:
#			for item in one_sent_list:
#				print 'surface=%s\tlem=%s\tpos=%s\t chunk=%s' % (item.surface, item.lem,item.pos,item.chunk)
			all_sent_list.append(one_sent_list)
#			print "EOS"
			one_sent_list = []
	return all_sent_list

if __name__ == '__main__':
	for name in glob.glob('71_GENIA_tagger_?.txt'):
		#print "name",name
		a = test72()
		list_print(a)