#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:03:37 Shin Kanouchi

"""(11) 「拡散希望」という文字列を含むツイートを抽出せよ．"""

import sys, re

for line in open("tweet.txt"):
    m = re.search('拡散希望', line)
    line = line.strip()
    if m == None:
        pass
    else:
        print line

