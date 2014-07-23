#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/15 13:18:39 Shin Kanouchi

import sys
from pymongo import Connection
import pymongo


con = Connection('127.0.0.1', 27017)#コネクション作成
db = con.nlp100_kanouchi#コネクションからtestデータベースを取得
col = db.tweets#testデータベースからfooコレクションを取得

q = unicode(sys.argv[1])
#db.tweets.find({},{"url":1})
for i in col.find({'bigram':q):
	print i

#db.test.update({"_id": "a00001"}, {$set:{"user_prof": { "work" : 0, "smorker" : 0 }}})