#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/08 11:58:08 Shin Kanouchi

import json
import sys
from pymongo import Connection
import pymongo

con = Connection('133.10.203.23', 27017)#コネクション作成
db = con.nlp100_kanouchi#コネクションからデータベースを取得
col = db.tweets#データベースからコレクションを取得

tweet_json = open(sys.argv[1],"r")
tweet = json.load(tweet_json)

for i in tweet:
	rt_url = ""
	reply_url= ""
	if 'retweeted_status' in i:#IDとスクリーンネームでurlが作れる
		rt_url = 'https://twitter.com/' + i['retweeted_status']['user']['screen_name'] + '/status/' + i['retweeted_status']['id_str']
	if i['in_reply_to_user_id'] is not None:
		reply_url = 'https://twitter.com/' + i['in_reply_to_screen_name'] + '/status/' + i['in_reply_to_user_id_str']
	url = 'https://twitter.com/' + i['user']['screen_name'] + '/status/' +  i['id_str']
	col.insert({'url':url,'date':i['created_at'],'user':i['id'],'nickname':i['user']['name'],'body':i['text'],'rt_url':rt_url,'reply_url':reply_url,'freq_rt':i['retweet_count'],})

#for i in col.find():
#	print i
"""
mongod --config mongodb.config
別のタブで
mongo
show dbs
use nlp100_kanouchi
db.tweets.drop()
db.tweets.find()
"""
