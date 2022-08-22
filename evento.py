#!/usr/bin/python
#-*- coding: utf-8 -*-

from Entities.Evento_interface import Evento_interface


class Evento(Evento_interface):
    def __init__(self, _detalles, _link, _nombre):
        self.detalles = _detalles
        self.link = _link
        self.nombre = _nombre
 
    def getDetalles(self):
        return self.detalles
 
    def getLink(self):
        return self.link

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, _nombre):
        self.nombre = _nombre

    def setDetalles(self, _detalles):
        self.detalles = _detalles 
    
    def setLink(self, _link):
        self.link = _link
    
    def show(self): 
        print("Nombre del evento: ", self.nombre) 
        print("Enlace al evento: ", self.link)
        print("Detalles del evento: ", self.detalles)
        
