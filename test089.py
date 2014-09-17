#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/07/15 13:18:39 Shin Kanouchi

import sys
from pymongo import Connection
import pymongo

con = Connection('127.0.0.1', 27017)
db = con.nlp100_kanouchi
col = db.tweets

q = unicode(sys.argv[1])
for i in col.find({'bigram':q):
	print i