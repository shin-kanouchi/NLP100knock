#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/15 12:44:06 Shin Kanouchi

from pymongo import Connection
import pymongo

con = Connection('127.0.0.1', 27017)
db = con.nlp100_kanouchi
col = db.tweets

for i in col.find():
	bi_list = []
	prev = '<s>'
	for uni in i['body']:
		bi = prev + uni
		bi_list.append(bi)
		prev = uni
	i['bigram'] =  bi_list
	print i['bigram']
	col.save(i)

col.created_index([("bigram",ASCENDING)])
con.disconnect()
