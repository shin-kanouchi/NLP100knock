#!/usr/bin/python
# -*-coding:utf-8-*-
"""
標準入力からタブ区切り形式のテキスト（address.txt）を読み込み，以下の内容を標準出力に書き出すプログラムを実装せよ．また，ヒントに挙げたツールを用いても，同じ内容が得られることを確認せよ
(1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．"""

import sys
print sum(1 for line in open(sys.argv[1]))

