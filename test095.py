#!/usr/bin/python
#-*-coding:utf-8-*-

import xml.sax
import xml.sax.handler
import sys
from xml.sax.handler import ContentHandler

class printNameHandler(ContentHandler):
    def __init__(self):
        self.flag = False
        self.title_name = ""

    def startElement(self, name, attrs):#attrsにredirectのidが入っている
        if name == "redirect":
            print self.title_name.encode("utf-8")+ "\t" + attrs.getValue("title").encode("utf-8")

        if name == "title":
            self.flag = True

    def endElement(self, name):
        if name == "title":
            self.flag = False

    def characters(self, data):
        if self.flag:
            self.title_name = data
            self.flag = False

def main(text):
    parser = xml.sax.make_parser()
    parser.setContentHandler(printNameHandler())
    print parser.parse(text)

if __name__=="__main__":
    main(sys.argv[1])
