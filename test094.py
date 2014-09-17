#!/usr/bin/python
#-*-coding:utf-8-*-

import xml.sax
import xml.sax.handler
import sys
from xml.sax.handler import ContentHandler

class printNameHandler(ContentHandler):
    def __init__(self):
        self.flag = False

    def startElement(self, name, attrs):
        if name == "title":
            self.flag = True

    def endElement(self, name):
        if name == "title":
            self.flag = False

    def characters(self, data):
        if self.flag:
            print data.encode("utf-8")

def main(text):
    parser = xml.sax.make_parser()
    parser.setContentHandler(printNameHandler())
    print parser.parse(text)

if __name__=="__main__":
    main(sys.argv[1])
