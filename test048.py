#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 18:28:36 Shin Kanouchi
"""(48) 標準入力から読み込んだ各行の文字列の頻度を求めるプログラムを書き，(47)のプログラムと組み合わせることによって，文章中に出現する各動詞の出現頻度を求めよ．さらに，出現頻度の高い順に動詞を並べよ．"""

import re
from collections import Counter
list_dict=[]
i=0
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
for line in open("japanese_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		if item[1] == "動詞":
			list_dict.append(item[7])

counter = Counter(list_dict)
for word, cnt in sorted(counter.most_common(),key=lambda x:x[1],reverse = True):
	print word, cnt