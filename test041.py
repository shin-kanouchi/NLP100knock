#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 12:49:27 Shin Kanouchi
"""日本語の文章japanese.txtに対して，以下の処理を行え．
(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．"""
import MeCab
doc = []
mc = MeCab.Tagger("mecabrc")
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

for line in open("japanese_tail10.txt"):
	one_sent = []
	line = mc.parse(line.strip())
	itemlist = line.strip().split("\n")
	for item in itemlist:
		if item == "EOS" or item == "":
			break
		surface,item2 = item.strip().split("\t")
		item3 = item2.split(",")
		dict = {'surface':surface, 'base' : item3[6] ,'pos':item3[0],'pos1':item3[1]}
		one_sent.append(dict)
	doc.append(one_sent)
