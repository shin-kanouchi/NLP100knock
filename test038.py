#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/27 14:55:39 Shin Kanouchi

from collections import Counter
cnt,context_cnt = Counter(),Counter()

for line in open('retest37.txt'):
	list1 = line.strip().split('\t')
	cnt[str(list1[1])+"\t"+str(list1[2])] += 1 #バイグラムの分母と分子
	context_cnt[str(list1[1])] += 1

for ngram in cnt:
	list2 = ngram.strip().split('\t')
	pro=float(cnt[ngram])/context_cnt[list2[0]]
	print (str(pro)+"\t"+ngram)