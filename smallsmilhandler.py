#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):

    def __init__(self):
        self.lista_etiq = []
        self.dicc = {'root-layout': ['width', 'height', 'background-color'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'begin', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        if name in self.dicc:
            dicc_nuevo = {}
            for atributo in self.dicc[name]:
                dicc_nuevo[atributo] = attrs.get(atributo, " ")
                dicc_completo = {name: dicc_nuevo}
            self.lista_etiq.append(dicc_completo)

    def get_tags(self):
        return self.lista_etiq


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
    print(cHandler.get_tags())
