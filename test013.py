#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/13 14:13:22 Shin Kanouchi
"""(13) 非公式RTのツイートの中で，RT先へのコメント部分のみを抽出せよ．"""
import sys,re
from collections import defaultdict

def tweet_id_text_dict():
    tweet_dict = defaultdict(list)
    tweet,name = "",""
    re_acount = re.compile(r"([0-9a-zA-Z_]{1,15}) : ")#宣言
    for line in open("tweet.txt"):
        m = re_acount.match(line)
        if m == None:
            tweet = tweet +line
        else:
            if name == "":
                pass
            else:
                tweet = tweet[:-1]
                tweet_dict[name].append(tweet)
            name = m.group(1)
            tweet = line[len(m.group()):]
    return tweet_dict

def open_dict_RT(tweet_dict):
    re_hikousiki = re.compile(r"(.+) RT @")
    for k, v in sorted(tweet_dict.items()):#defaultdictをkey順に展開
        for v2 in v:#defaultdictの中のlistを展開
            m = re_hikousiki.match(v2)
            if m == None:
                pass
            else:
                print m.group(1)

if __name__ == '__main__':
    dict = tweet_id_text_dict()
    open_dict_RT(dict)
