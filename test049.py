#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 18:28:36 Shin Kanouchi
"""(49) (48)の出力を利用して，
文字列の頻度を横軸，
その文字列の異なり数（種類数）を縦軸として，
ヒストグラムをプロットせよ．
なお，プロットにはgnuplotやmatplotlibを用い，
グラフを画像ファイルとして保存せよ．"""
import matplotlib.pyplot as plt

def read_file(open_file):
	word_dict = {}
	for line in open(open_file):
		w, i = line.strip().split()
		word_dict[w] = int(i)
	return word_dict

def main():
	fig = plt.figure()# プロット領域
	ax = fig.add_subplot(111)
	ax.hist(word_dict.values(), bins=len(word_dict.values()), range=(0, 150))
	plt.title('title')
	plt.ylabel(' Type(kotonari) ')
	plt.xlabel(' Frequency ')
	ax.set_xlim(0, 150)
	ax.set_ylim(0, 100)
	plt.savefig("plt_retest49.eps")
	plt.show()

if __name__ == '__main__':
	word_dict = read_file("japanese_48.txt")
	main()