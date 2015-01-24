#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/20 16:45:56 Shin Kanouchi
"""(71) ５つのファイル（英語のテキスト）にGENIA taggerを適用せよ．
GENIA taggerは１文１行形式の入力を受け取るので，22のプログラムを再利用せよ．
また，入力ファイルはgzipで圧縮されていることに注意せよ．"""
import sys,re,glob
sys.path.append('/Users/shin/work/nlp100knock/geniatagger-python-master')
from geniatagger import *
tagger = GeniaTagger('/Users/shin/work/nlp100knock/geniatagger-3.0.1/geniatagger')

def main():
	for name in glob.glob('english_?.txt'):
		f1= open("71_GENIA_tagger_"+name[-5:], 'w')
		print "name", name
		for line in open(name):
			line = line.strip()
			item = re.split(r'(\.) ([A-Z])|(\[[0-9]+\]+) ([A-Z])', line)
			while None in item: 
				item.remove(None)
			for w in range( len(item) ):
				w_tagger = None
				if w == 0 and len(item) == 1 : #最初の文
					#print item[w]
					w_tagger = tagger.parse(item[w])
				elif w == 0 : #最初の文
					w2 = item[w]
				elif w ==1: #最初のピリオドまで
					w2 = w2 + item[w]
					w_tagger = tagger.parse(w2)
				elif w % 3 == 2:
					w2 = item[w]
				elif w == (len(item)-1): #最後の文
					w2 = w2 + item[w]
					w_tagger = tagger.parse(w2)
				elif w % 3 == 0:
					w2 = w2 + item[w]
				else:
					w2 = w2 + item[w]
					w_tagger = tagger.parse(w2)
				if w_tagger:
					for w in w_tagger:
						f1.write("\t".join(w) + "\n")
					f1.write("\n")
		f1.close()


if __name__ == '__main__':
	main()
