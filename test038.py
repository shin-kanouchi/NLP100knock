
#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:55:39 Shin Kanouchi
"""(38) (37)の出力を読み込み，ある単語wに続く単語zの条件付き確率P(z|w)を求めよ．
ただし，出力形式は"(条件付き確率)\t(現在の単語)\t(次の単語)"とせよ．"""

from collections import Counter
cnt,context_cnt = Counter(),Counter()

for line in open('test037.txt'):
	list1 = line.strip().split('\t')
	cnt[str(list1[1])+"\t"+str(list1[2])] += 1 #バイグラムの分母と分子
	context_cnt[str(list1[1])] += 1

for ngram in cnt:
	list2 = ngram.strip().split('\t')
	pro=float(cnt[ngram])/context_cnt[list2[0]]
	print (str(pro)+"\t"+ngram)