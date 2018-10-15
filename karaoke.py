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
            dicc = elemento[1].items()
            for nombre, valor in dicc:
                linea = linea + "\t" + nombre + "=" + '"' + valor + '"'
            linea = linea + "\n"
        return linea

    def to_json(self, fichero, fjson=""):
        if fjson == "":
            fjson = fichero.split(".")[0] + ".json"
        with open(fjson, 'w') as fichero_json:
            json.dump(self.info, fichero_json, sort_keys=True, indent=4)

    def do_local(self):
        for elemento in self.info:
            dicc = elemento[1]
            for atributo in dicc:
                if atributo == 'src':
                    if dicc[atributo].split("/")[0] == "http:":
                        urllib.request.urlretrieve
                        (dicc[atributo], dicc[atributo].split("/")[-1])
                        dicc[atributo] = dicc[atributo].split("/")[-1]


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        karaoke = KaraokeLocal(fichero)
        print(karaoke)
        karaoke.to_json(fichero)
        karaoke.do_local()
        karaoke.to_json(fichero, "local.json")
        print(karaoke)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
