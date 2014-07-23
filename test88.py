#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/15 12:44:06 Shin Kanouchi

import json
import sys
from pymongo import *#Connection
import pymongo


con = Connection('127.0.0.1', 27017)#コネクション作成
#con = Connection('133.10.203.23', 27017)#コネクション作成
db = con.nlp100_kanouchi#コネクションからtestデータベースを取得
col = db.tweets#testデータベースからfooコレクションを取得

#tweet_json = open(sys.argv[1],"r")
#tweet = json.load(tweet_json)

for i in col.find():
	bi_list = []
	prev = '<s>'
	for uni in i['body']:
		bi = prev + uni
		bi_list.append(bi)
		prev = uni
	"""for j in range(1,len(i['body'])):
		bi = i['body'][j-1]+i['body'][j]
		bi_list.append(bi)"""
	i['bigram'] =  bi_list
	print i['bigram']
	col.save(i)

col.created_index([("bigram",ASCENDING)])
con.disconnect()
