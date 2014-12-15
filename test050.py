#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 18:28:36 Shin Kanouchi
"""(50) (48)の出力を利用して，
文字列の出現頻度の順位（高い順）を横軸，
その出現頻度を縦軸として，プロットせよ．"""
import matplotlib.pyplot as plt

def main():
	dict={}
	listx,listy=[],[]
	j=0
	for line in open("japanese_48.txt"):
		w,i = line.strip().split(" ")
		dict[w]=int(i)
		#if j < 100:
		listx.append(j)
		listy.append(int(i))
		j+=1

	plt.plot(listx,listy)
	plt.title('title')
	plt.xlabel(' words ')
	plt.ylabel(' Frequency ')
	plt.xlim(0,100)
	plt.ylim(0,300)
	plt.show()

if __name__ == '__main__':
	main()