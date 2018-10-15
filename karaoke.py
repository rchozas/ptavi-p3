#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.info = cHandler.get_tags()
        
        
    def __str__(self):
        linea = " "
        for elemento in self.info:
            linea = linea + elemento[0]
            atributos = elemento[1].items()
            for nombre, valor in atributos:
                linea = linea + "\t" + nombre + "=" + '"' + valor + '"'
            linea = linea + "\n"
        return linea 
        
    
        
if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

