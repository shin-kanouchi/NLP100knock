#!/usr/bin/python
#-*-coding:utf-8-*-
"""(9) 各行を２コラム目，１コラム目の優先順位で
辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．"""
import sys
import test008 

list1 = test008.test008_1()
for w1, w2 in sorted(list1, key=lambda x: (x[1], x[0]), reverse = True ):
	print "%s\t%s" % (w1, w2)