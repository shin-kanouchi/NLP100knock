#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/03 17:42:54 Shin Kanouchi
"""(47) (42)から(46)までの処理を１つのプログラムに統合し，処理内容をコマンドライン引数でOn/Offできるようにせよ．コマンドライン引数の処理には，optparseモジュールを用い，オプションには適当な名前（例えば(42)は--verbなど）とドキュメント（-hを引数にすることで表示される）を書け．"""
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import sys,optparse,re
parser = optparse.OptionParser()

parser.add_option('-a','--i42', action='store_true',help="kadai42_do-shi",default=False)#store_trueで引数を取らない設定になる
parser.add_option('-b','--i43', action='store_true',help="kadai43_do-shi_genke-",default=False)
parser.add_option('-c','--i44', action='store_true',help="kadai44_sahen_me-shi",default=False)
parser.add_option('-d','--i45', action='store_true',help="kadai45_A_no_B",default=False)
parser.add_option('-e','--i46', action='store_true',help="kadai46_me-shi_rensetsu",default=False)
options, args = parser.parse_args()

item_list,list_meisi=[],[]
for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		item_list.append(item)
			#-------------------------------------------------------42
		if options.i42 == 1:
			if item[1] == "動詞":
				print item[0]
		#-------------------------------------------------------43
		if options.i43 == 1:
			if item[1] == "動詞":
				print "基本形=",item[7]
		#-------------------------------------------------------44
		if options.i44 == 1:
			if item[2] == "サ変接続":
				print item[2],item[0]
		#-------------------------------------------------------45
		if options.i45 == 1:
			i = len(item_list)-1
			if i>1 and item_list[i-2][1]=="名詞" and item_list[i-1][0]=="の" and item_list[i][1]=="名詞":
				print item_list[i-2][0],item_list[i-1][0], item_list[i][0]
		#-------------------------------------------------------46
		if options.i46 == 1:
			if item[1] == "名詞":
				list_meisi.append(item[0])
			elif len(list_meisi) > 1:
				for meisi in list_meisi:
					print meisi,
				print ""
				list_meisi=[]
			else:
				list_meisi=[]
