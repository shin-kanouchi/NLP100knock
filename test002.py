#!/usr/bin/python
# -*-coding:utf-8-*-

"""(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．"""
import sys
for line in open(sys.argv[1]):
    print(line.replace("	"," ")),