#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/09 18:23:01 Shin Kanouchi
"""(62) 61で作成した各ファイルから，名詞句（文節中の名詞の連接）を抜き出して，個別のファイルに格納せよ．"""
import re,glob
list_meisi=[]

for name in glob.glob('61_output_japanese_?.txt'):
	f1= open("62_output_"+name[10:],'w')
	print name
	for line in open(name):
		if "\t" in line:
			item = re.split(r"\t|,",line.strip())
			if item[1] == "名詞":
				list_meisi.append(item[0])
			elif len(list_meisi) > 0:
				for meisi in list_meisi:
					f1.write(meisi)#(meisi+" ")
				f1.write("\n")
				list_meisi=[]
			else:
				list_meisi=[]
		elif "* " in line or "EOS" in line:
			if len(list_meisi) > 0:
				for meisi in list_meisi:
					f1.write(meisi)#(meisi+" ")
				f1.write("\n")
				list_meisi=[]
			else:
				list_meisi=[]
	f1.close()