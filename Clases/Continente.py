from .Clase_Base import *

class Continente(Clase_Base):

    def __init__(self, nombre, codigo, coordenadas):
        Clase_Base.__init__(self, nombre, codigo)
        self.Coordenadas = coordenadas
        self.Lista_Paises = []