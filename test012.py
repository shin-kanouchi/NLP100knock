#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:11:29 Shin Kanouchi

"""(12) 「なう」という文字列で終わるツイートを抽出せよ．"""

import sys, re

for line in open("tweet.txt"):
    line = line.strip()
    if line.endswith('なう') == True:
        print line
