#!/usr/bin/python
# -*-coding:utf-8-*-

"""(1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．"""

import sys

print sum(1 for line in open(sys.argv[1]))

