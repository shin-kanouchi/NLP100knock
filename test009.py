#!/usr/bin/python
#-*-coding:utf-8-*-
"""(9) 各行を２コラム目，１コラム目の優先順位で辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．"""
import sys
from test008 import *

list = test8_1()
list.sort(key=lambda x:(x[1],x[0]) ,reverse = True )

for i in range(len(list)):
	print list[i][0]+"\t"+list[i][1]
