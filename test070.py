#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/14 05:02:40 Shin Kanouchi
"""(70) 68の結果を用い，最長距離法（furthest neighbor method; complete link method）で名詞句のクラスタリングを行い，クラスタを抽出せよ．"""
from collections import defaultdict
def dist_two_class(class1,class2):
	cos_min =1.0
	for word1 in class1:
		for word2 in class2:
			if not word1+" "+word2 in dict:
				dict[word1+" "+word2] = 1.0
			if dict[word1+" "+word2] < cos_min:
				cos_min = dict[word1+" "+word2]
	if cos_min ==1:
		cos_min = 0
	return cos_min


def test070(argv1):
	dict = defaultdict(lambda: 0)
	word_set =set([])
	for line in open("68_output.txt"):
		item = line.strip().split('\t')
		dict[item[1]+' '+item[2]]=float(item[0])
		dict[item[2]+' '+item[1]]=float(item[0])
		word_set.add(item[1])
		word_set.add(item[2])

	#初期クラスの作成
	class_list = []
	word_dic = defaultdict(lambda: 0)
	for word in word_set:
		word_dic = [word]
		class_list.append(word)

	while len(class_list) > int(argv1):
		d_max = 0
		best_class = tuple
		for class1 in class_list:
			for class2 in class_list:
				if class1 != class2:
					d = dist_two_class(class1, class2)
					if d >= d_max:
						d_max = d_max
						best_class = (class1, class2)
		class1,class2 = best_class[0], best_class[1]
		class_list.append(best_class[0] + best_class[1])
		class_list.remove(best_class[0])
		class_list.remove(best_class[1])

		print len(dict)
		maxward1, maxward2 = max(dict.items(), key=lambda x:x[1])[0].split()
		print maxward1, maxward2
		"""
		for maxward in maxwards:
			for word in ward_set:
				if (maxward+word or word+maxwards) in dict:"""

"""
	for k,v in sorted(dict.items(),key=lambda x:x[1],reverse = True):
		print k,v
		print k.split()[1]"""

if __name__ == '__main__':
	import sys
	test070(sys.argv[1])
