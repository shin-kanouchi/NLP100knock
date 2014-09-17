#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 14:08:05 Shin Kanouchi
import sys,MeCab
mc = MeCab.Tagger("mecabrc")

for line in open("japanese_tail10.txt"):
	one_sent = []
	line = mc.parse(line.strip())
	itemlist = line.strip().split("\n")
	for item in itemlist:
		if item == "":
			break
		print item