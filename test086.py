#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/15 12:28:04 Shin Kanouchi

import sys
from pymongo import Connection
import pymongo

con = Connection('127.0.0.1', 27017)#コネクション作成
db  = con.nlp100_kanouchi#コネクションからデータベースを取得
col = db.tweets#データベースからコレクションを取得

for i in col.find({'url':sys.argv[1]}):
	print i['body']