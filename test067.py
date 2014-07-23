#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/17 17:43:09 Shin Kanouchi
"""(67) 66の出力の各行を名詞句の（疎）ベクトルとみなし，「日本」と「我が国」のベクトル間の内積（コサイン類似度）を求めよ．"""
from collections import defaultdict

def make_vector(open_file):
	word_dict = defaultdict(list)
	for line in open(open_file):
		for item in line.strip().split("\t"):
			kakari_value = item.split(" : ")
			if len(kakari_value) == 1:
				word = kakari_value[0]
			else:
				word_dict[word].append((kakari_value[0],kakari_value[1]))
	return word_dict

def calculate_vector(word_dict,argv1,argv2):
	i=0
	assert argv1 and argv2 in word_dict, "error : sys.argv[1] or sys.argv[2] is not found in dict"
	for word1,v1 in word_dict[argv1]:
		for word2,v2 in word_dict[argv2]:
			if word1 == word2:
				i += float(v1) * float(v2)
				#print word1," is  match!!!  ","i+=",v1,"*",v2,"i =", i
	return str(i)

if __name__ == '__main__':
	import sys
	assert len(sys.argv) > 2, "error : sys.argv[2] is not found"
	word_dict = make_vector("66_output.txt")
	print "ans= ",calculate_vector(word_dict,sys.argv[1],sys.argv[2])