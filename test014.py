#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:29:40 Shin Kanouchi
"""(14) ツイッターのユーザー名（@で始まる文字列）を抽出せよ．"""

import sys,re

def tweet_user():
	r = re.compile(r"(@[0-9a-zA-Z_]{1,15})")#宣言
	for line in open("tweet.txt"):
	    m = r.search(line)
	    if m == None:
	        pass
	    else:
	        print m.group(0)

if __name__ == '__main__':
    tweet_user()
