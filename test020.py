#!/usr/bin/python
#-*-coding:utf-8-*-
"""(20) ツイートから絵文字らしき文字列を抽出せよ．"""
def kaomozi():
	import re
	r = re.compile(r"\([^一-龥ぁ-んァ-ヴ]{3,6}\)")#3~6文字の日本語以外
	#r2 = re.compile(r"\([^0-9]{3,6}\)")
	#r3 = re.compile(r"\([^a-zA-Z]{3,6}\)")

	for line in open("tweet.txt"):
		if r.search(line):# and r2.search(line)and r3.search(line):
			print r.search(line).group(0)

if __name__ == '__main__':
	kaomozi()