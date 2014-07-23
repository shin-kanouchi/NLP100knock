#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/06 14:03:28 Shin Kanouchi

"""(60) (57)の出力を「係り元」→「係り先」の有向グラフとみなし，Graphvizを使ってグラフを描画せよ．すなわち，(57)の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい"""

"""出力形式
digraph knock60{
\t"" -> "";
}"""
def test60():
	print "digraph knock60{"
	for line in open("test57.txt"):
		item = line.replace('\"',r'\"')
		item = item.strip().split(' ')
		print '\t"%s" -> "%s";' % (item[0],item[1])
	print "}"


if __name__ == '__main__':
	test60()
