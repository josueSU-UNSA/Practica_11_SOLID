#!/usr/bin/python
#-*- coding: utf-8 -*-
#0000
from Usuario import Usuario

#STyle Objetos e interacciones de objetos


# Principio I el Asistente que desciende de usuario solo puede realizar su accion correspondiente 
# Y no comparte acciones con su clase hermana Ponente
class Asistente(Usuario):
    def autentificar(self):
        return True

