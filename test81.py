#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/08 11:58:08 Shin Kanouchi
import json
import sys
from pymongo import Connection
import pymongo

con = Connection('133.10.203.23', 27017)#コネクション作成
db = con.nlp100_kanouchi#コネクションからtestデータベースを取得
col = db.tweets#testデータベースからfooコレクションを取得

tweet_json = open(sys.argv[1],"r")
tweet = json.load(tweet_json)

for i in tweet:
	rt_url = ""
	reply_url= ""
	if 'retweeted_status' in i:
		rt_url = 'https://twitter.com/' + i['retweeted_status']['user']['screen_name'] + '/status/' + i['retweeted_status']['id_str']
	if i['in_reply_to_user_id'] is not None:
		reply_url = 'https://twitter.com/' + i['in_reply_to_screen_name'] + '/status/' + i['in_reply_to_user_id_str']
	url = 'https://twitter.com/' + i['user']['screen_name'] + '/status/' +  i['id_str']
	col.insert({'url':url,'date':i['created_at'],'user':i['id'],'nickname':i['user']['name'],'body':i['text'],'rt_url':rt_url,'reply_url':reply_url,'freq_rt':i['retweet_count'],})
	#print reply_url
#for i in col.find():
#	print i
"""
for tweet_dict in tweet:
	for k,v in tweet_dict.items():
		print k,v
		#if k == 'source':
		#	print v
		print'--------------'"""
"""
mongod --config mongodb.config
別のタブで
mongo
show dbs
use nlp100_kanouchi
db.tweets.drop()
db.tweets.find()
"""
"""
82
db.tweets.ensureIndex({"date":1})
db.tweets.getIndexes()
db.tweets.find({"nickname" : "あやか"})
db.tweets.find({},{"url":1})

IDとスクリーンネームでurlが作れる
retweeted_statusがあるかないか


85
db.tweets.find({"nickname" : "あやか"}).sort({'freq_rt':-1}).limit(10)
{ "_id" : ObjectId("53c4b2e4fad19618ed3b7a4f"), "body" : "今寝たら負けなんだよ！知ってる。😶", "date" : "Sun Jul 06 16:58:12 +0000 2014", "rt_url" : "", "freq_rt" : 0, "user" : NumberLong("485830082707988481"), "url" : "https://twitter.com/ayakas_s/status/485830082707988481", "nickname" : "あやか", "reply_url" : "" }
"""
