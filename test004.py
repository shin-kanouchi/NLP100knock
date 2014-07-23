#!/usr/bin/python
#-*-coding:utf-8-*-
"""(4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．"""
import sys

list1,list2= [],[]

for line1 in open(sys.argv[1]):
	list1.append(line1.strip()) #listの最後尾に入れる

for line2 in open(sys.argv[2]):
	list2.append(line2.strip())

if len(list1) != len(list2):
  print >>sys.stderr, "Total lines are not same."

for i in range(len(list1)):
	print list1[i] + "	" + list2[i]

"""
    for a ,b in zip(list1,list2): ←zipで２つの配列をカップリングさせる
	print a +" "+b
"""

