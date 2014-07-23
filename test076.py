#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/30 16:33:06 Shin Kanouchi
"""(76) 75で作成したプログラムをdata00.genia.gz～data04.genia.gzに適用し，学習データdata00.f～data04.fを作成せよ．"""
from test072 import *
class fature:
	def __init__(self,pre_w,pre_pos,head_w,f_pos):#pre_w,pre_pos,head_w,one_chunk.pos
		self.pre_w   = pre_w
		self.pre_pos = pre_pos
		self.head_w  = head_w
		self.f_pos   = f_pos

def find_head(w):
	if w == 'a' or w =='an':
		return 'A'
	elif w =='the':
		return w.upper()
	else:
		return "NONE"

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

def make_fature(w, fatures,next_w,next_pos, hpos):#w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
	item    = w.split()
	if fatures.head_w != "NONE" and len(item) > 2: i=2
	else: i=1
	w_0     = '\t'.join(item[i:])#ok
	fw      = item[i]#ok
	fpos    = fatures.f_pos
	hw      = item[-1]#ok
	#print '%s\n%s\tw[0]= %s\thw= %s\thpos= %s\tfw= %s\tfpos= %s\tw[-1]= %s\tpos[-1]= %s\tw[1]= %s\tpos[1]= %s\t' % (w,fatures.head_w,w_0,hw,hpos,fw,fpos,fatures.pre_w,fatures.pre_pos,next_w,next_pos)
	f1.write('%s\n%s w[0]=%s hw=%s hpos=%s hw|hpos=%s|%s fw=%s fpos=%s fw|fpos=%s|%s w[-1]=%s pos[-1]=%s w[1]=%s pos[1]=%s\n' % (w,fatures.head_w,w_0,hw,hpos,hw,hpos,fw,fpos,fw,fpos,fatures.pre_w,fatures.pre_pos,next_w,next_pos))


def test75(all_sent_list):
	for one_sent_list in all_sent_list:
		w = ''
		pre_w = "None"
		pre_pos = "None"
		for one_chunk in one_sent_list:
			if one_chunk.chunk == "B-NP":
				if w.startswith('#'):
					make_fature(w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
				head_w  = find_head(one_chunk.surface.lower())
				fatures = fature(pre_w,pre_pos,head_w,one_chunk.pos)
				w       = '# ' + one_chunk.surface
			elif one_chunk.chunk == "I-NP" and w !='':
				if fatures.head_w != "NONE":
					fatures.f_pos = one_chunk.pos
				w = w +' '+ one_chunk.surface
			elif w != '':
				make_fature(w,fatures,one_chunk.surface,one_chunk.pos,pre_pos)
				w = ''
			else: pass
			pre_w = one_chunk.surface
			pre_pos = one_chunk.pos


if __name__ == '__main__':
	for name in glob.glob('71_GENIA_tagger_?.txt'):
		f1= open("76_output"+name[-5]+".f",'w')
		all_sent_list=test72(name)
		test75(all_sent_list)
		f1.close()

