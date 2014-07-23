#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 18:28:36 Shin Kanouchi
"""(49) (48)の出力を利用して，文字列の頻度を横軸，その文字列の異なり数（種類数）を縦軸として，ヒストグラムをプロットせよ．なお，プロットにはgnuplotやmatplotlibを用い，グラフを画像ファイルとして保存せよ．"""
import matplotlib.pyplot as plt
dict={}

for line in open("japanese_48.txt"):
	w,i = line.strip().split(" ")
	dict[w]=int(i)#ここのいんとないとできない
#for i in dict.values():
#	print i

fig = plt.figure()# プロット領域（1x1分割の1番目に領域を配置せよという意味）
ax = fig.add_subplot(111)# ヒストグラム（normedをTrueで指定すると確率表示になる）
ax.hist(dict.values(), bins=len(dict.values()), range=(0, 150))#plt.plot(cnt.items(),len())
plt.title('title')
plt.ylabel(' kotonarisu- ')
plt.xlabel(' hindo ')
ax.set_xlim(0, 150)
ax.set_ylim(0, 100)
plt.savefig("plt_retest49.eps")
plt.show()