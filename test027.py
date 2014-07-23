#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:24:21 Shin Kanouchi
"""(27) (10)のプログラムを呼び出すことで，頻度の高い英単語トップ100（単語と頻度がソートされたもの）を作成せよ．"""
from retest10 import *
list=[]

for line in open('medline3.txt'):
	list.append(line.strip())

retest10_1(list)
