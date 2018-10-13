#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSmilHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.dic_etiq = {'root-layout': ['width', 'height', 'background-color'],
                        'region': ['id','top','bottom', 'left', 'right'],
                         'img': ['src', 'region', 'begin', 'dur'],
                        'audio': ['src', 'begin', 'dur'],
                        'textstream'['src', 'region']}
    def get_tags(self):


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open())
