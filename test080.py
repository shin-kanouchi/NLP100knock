#!/usr/bin/python
#-*-coding:utf-8-*-
"""
(80) 入力された英語の文に対して，各名詞句の冠詞のタイプを推定し，
誤りがあれば訂正を行うシステムを構築せよ
"""
from collections import defaultdict

class Morph:
	def __init__(self, surface, lem, pos, chunk):
		self.surface = surface
		self.lem     = lem
		self.pos     = pos
		self.chunk   = chunk
class fature:
	def __init__(self, pre_w, pre_pos, head_w, f_pos):
		self.pre_w   = pre_w
		self.pre_pos = pre_pos
		self.head_w  = head_w
		self.f_pos   = f_pos

def find_head(w):
	if w == 'a' or w =='an':
		return 'A'
	elif w == 'the':
		return w.upper()
	else:
		return "NONE"

def make_fature(w, fatures, next_w, next_pos, hpos):#w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
	item = w.split()
	if fatures.head_w != "NONE" and len(item) > 2: 
		i = 2
	else: 
		i = 1
	w_0     = '\t'.join(item[i:])#ok
	fw      = item[i]#ok
	fpos    = fatures.f_pos
	hw      = item[-1]#ok
	#print '%s\n%s\tw[0]= %s\thw= %s\thpos= %s\tfw= %s\tfpos= %s\tw[-1]= %s\tpos[-1]= %s\tw[1]= %s\tpos[1]= %s\t' % (w,fatures.head_w,w_0,hw,hpos,fw,fpos,fatures.pre_w,fatures.pre_pos,next_w,next_pos)
	f1.write('%s\n%s w[0]=%s hw=%s hpos=%s hw|hpos=%s|%s fw=%s fpos=%s fw|fpos=%s|%s w[-1]=%s pos[-1]=%s w[1]=%s pos[1]=%s\n' \
		% (w, fatures.head_w, w_0, hw, hpos, hw, hpos, fw, fpos, fw, fpos, fatures.pre_w, fatures.pre_pos, next_w, next_pos))

def test75(one_sent_list):
	w = ''
	pre_w = "None"
	pre_pos = "None"
	for one_chunk in one_sent_list:
		if one_chunk.chunk == "B-NP":
			if w.startswith('#'):
				make_fature(w, fatures, one_chunk.surface, one_chunk.pos, pre_pos)
			head_w = find_head(one_chunk.surface.lower())
			fatures = fature(pre_w, pre_pos, head_w, one_chunk.pos)
			w    = '# ' + one_chunk.surface
		elif one_chunk.chunk == "I-NP" and w != '':
			if fatures.head_w != "NONE":
				fatures.f_pos = one_chunk.pos
			w = w +' '+ one_chunk.surface
		elif w !='':
			make_fature(w, fatures, one_chunk.surface, one_chunk.pos, pre_pos)
			w = ''
		else: 
			pass
		pre_w = one_chunk.surface
		pre_pos = one_chunk.pos

def test72(item):
	one_sent_list = []
	for i in range(len(item)/5):
		#print item[5*i]
		one_sent_list.append(Morph(item[5*i], item[5*i+1], item[5*i+2], item[5*i+3]))
	return one_sent_list

if __name__ == '__main__':
	import sys
	one_sent_list=test72(sys.argv[1:])
	f1 = open("80_output_genear_noun.f", 'w')
	test75(one_sent_list)
	f1.close()
