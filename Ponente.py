#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuario import Usuario
from Usuario import Usuario
# Principio I el Ponente que desciende de usuario solo puede realizar su accion correspondiente 
# Y no comparte acciones con su clase hermana Asistente
class Ponente(Usuario, Usuario):
    def discurso(self,discurso):
        return discurso

