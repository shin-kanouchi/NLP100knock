#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/27 15:35:26 Shin Kanouchi
"""(75) 74で作成したプログラムを改変し，以下の11種類の素性を抽出・表示するプログラムを実装せよ．ただし，これらの素性はタブ区切り形式で"# (名詞句)\n(冠詞タイプ)\t(タブ区切り形式の素性)\n"という形式で出力せよ．例えば，"A major challenge is [the limited number] of NOE restraints ..."の[]の部分の名詞句に対して，次の出力を得る（ただし"\"は実際にはここで改行しないことを表す）"""
"""hw=(末尾の単語)
hpos=(末尾の品詞)
hw|hpos=(末尾の単語)|(末尾の品詞)
fw=(先頭の単語)
fpos=(先頭の品詞)
fw|fpos=(先頭の品詞)|(先頭の単語)
w[0]=(名詞句の単語列)
w[-1]=(名詞句の１語前の単語)
pos[-1]=(名詞句の１語前の品詞)
w[1]=(名詞句の１語後の単語)
pos[1]=(名詞句の１語後の品詞)"""

from test072 import *

class fature:
	def __init__(self,pre_w,pre_pos,head_w,f_pos):#pre_w,pre_pos,head_w,one_chunk.pos
		self.pre_w = pre_w
		self.pre_pos = pre_pos
		self.head_w = head_w
		self.f_pos = f_pos
		#self.h_pos = h_pos

def find_head(w):
	if w == 'a' or w =='an' or w =='the':
		return w.upper()
	else:
		return "NONE"

def make_fature(w, fatures,next_w,next_pos, hpos):#w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
	item    = w.split()
	if fatures.head_w != "NONE" and len(item) > 2: i=2
	else: i=1
	w_0     = ' '.join(item[i:])#ok
	fw      = item[i]#ok
	fpos    = fatures.f_pos
	hw      = item[-1]#ok
	print '%s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s\tw[-1]=%s\tpos[-1]=%s\tw[1]=%s\tpos[1]=%s' % (w,fatures.head_w,w_0,hw,hpos,hw,hpos,fw,fpos,fw,fpos,fatures.pre_w,fatures.pre_pos,next_w,next_pos)

def test075(all_sent_list):
	for one_sent_list in all_sent_list:
		w = ''
		pre_w = "None"
		pre_pos = "None"
		for one_chunk in one_sent_list:
			if one_chunk.chunk == "B-NP":
				if w.startswith('#'):
					make_fature(w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
				head_w = find_head(one_chunk.surface.lower())
				fatures = fature(pre_w,pre_pos,head_w,one_chunk.pos)
				w    = '# ' + one_chunk.surface
			elif one_chunk.chunk == "I-NP" and w !='':
				if fatures.head_w != "NONE":
					fatures.f_pos = one_chunk.pos
				w = w +' '+ one_chunk.surface
			elif w !='':
				make_fature(w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
				w=''
			else: pass
			pre_w = one_chunk.surface
			pre_pos = one_chunk.pos

if __name__ == '__main__':
	all_sent_list=test072('71_GENIA_tagger_1.txt')
	test075(all_sent_list)
