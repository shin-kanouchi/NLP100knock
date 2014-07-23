#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:34:02 Shin Kanouchi
"""(15) ツイッターのユーザー名（例えば@xxxxxxx）を，そのユーザーのページへのリンク（<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>で囲まれたHTML断片）に置換せよ．"""
import sys,re

r = re.compile(r"@([0-9a-zA-Z_]{1,15})")#宣言
for line in open("tweet.txt"):
	if r.search(line):
		print re.sub('xxxxxx', r.search(line).group(1), r'<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>')#xxxxxxxをm.group(1)に置換