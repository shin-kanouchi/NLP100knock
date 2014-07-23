#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/05/20 14:19:35
"""１行１単語形式のテキストmedline.txt.sent.tokを用いて，以下の分析を行え．
(26) -nessと-lyの両方の派生語尾をとる単語をすべて抜き出せ．"""
import re

for line in open('medline3.txt'):
	m = re.match(r'.+ness|.+ly',line.strip())
	if m :
		print line.strip()