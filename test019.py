#!/usr/bin/python
#-*-coding:utf-8-*-

"""(19) 郵便番号・県名・市町村名の３要素を組で（まとめて）抽出せよ．"""
import re
r = re.compile(u"[一-龥ぁ-んァ-ヴ]{2,3}県.{1,6}市")#3〜６文字

for line in open("tweet.txt"):
	m = r.search(line.decode("utf-8"))
	if m :
		print m.group(0)
