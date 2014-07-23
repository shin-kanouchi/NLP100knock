#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 10:23:12 Shin Kanouchi
"""(61) コーパスディレクトリ中の各ファイルに対して，cabochaを適用し，適当なディレクトリに係り受け解析の結果を格納せよ．ただし，各ファイルの文字コードがUTF-16LEであること，文区切りを自前で行う必要があることに注意せよ．"""

import CaboCha,glob

def main():
	for name in glob.glob('japanese_?.txt'):#OSでもできる
		f1= open("61_output_"+name,'w')
		print name
		for line in open(name):
			Cabo = CaboCha.Parser('--charset=UTF8')
#			print Cabo.parse(line).toString(CaboCha.FORMAT_LATTICE),
			f1.write(Cabo.parse(line).toString(CaboCha.FORMAT_LATTICE))
		f1.close()

if __name__ == '__main__':
	main()

"""こっちでも可
shin:test kanouchishin$ CaboCha -f1 japanese_1.txt >61_output_japanese_1.txt
shin:test kanouchishin$ CaboCha -f1 japanese_2.txt >61_output_japanese_2.txt
shin:test kanouchishin$ CaboCha -f1 japanese_3.txt >61_output_japanese_3.txt
shin:test kanouchishin$ CaboCha -f1 japanese_4.txt >61_output_japanese_4.txt
shin:test kanouchishin$ CaboCha -f1 japanese_5.txt >61_output_japanese_5.txt
"""
