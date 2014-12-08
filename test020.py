#!/usr/bin/python
#-*-coding:utf-8-*-
"""(20) ツイートから絵文字らしき文字列を抽出せよ．"""

def kaomozi():
	import re
	r = re.compile(r"\([^一-龥ぁ-んァ-ヴ]{3,6}\)")#3~6文字の日本語以外
	#r = re.compile(r"[^一-龥ぁ-んァ-ヴ]{1,2}\([^一-龥ぁ-んァ-ヴ]{3,6}\)[^一-龥ぁ-んァ-ヴ]{1,2}")#3~6文字の日本語以外
	for line in open("tweet.txt"):
		m = r.search(line.strip()) 
		if m:
			print m.group(0)

if __name__ == '__main__':
	kaomozi()