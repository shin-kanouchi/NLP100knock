#!/usr/bin/python
#-*-coding:utf-8-*-

import xml.sax
import xml.sax.handler
import sys,re
from xml.sax.handler import ContentHandler

r = re.compile("\{\{Commonscat\|(.*)\}\}")

class printNameHandler(ContentHandler):
    def __init__(self):
        self.flag  = False
        self.flag2 = False
        self.title_name = ""
        self.long_text = ""

    def startElement(self, name, attrs):#attrsにredirectのidが入っている
        if name == "text":
            self.flag2 = True

        if name == "title":
            self.flag = True

    def endElement(self, name):
        if name == "title":
            self.flag = False
        if name == "text":
            self.flag2 = False
    def characters(self, data):
        if self.flag:
            self.title_name = data
        if self.flag2:
            m = r.search(data)
            if m:
               w = m.group(1).strip().split('|')
               print self.title_name,"の英語版タイトル",w[0]#self.title_name.encode("utf-8")+ "\t" + attrs.getValue("title").encode("utf-8")1
            #self.long_text = self.long_text + data

def main(text):
    parser = xml.sax.make_parser()
    parser.setContentHandler(printNameHandler())
    print parser.parse(text)

if __name__=="__main__":
    main(sys.argv[1])
