from .Continente import *

class Provincia(Clase_Base):

    def __init__(self, nombre, codigo, coordenadas, pertenece):
        Clase_Base.__init__(self, nombre, codigo)
        self.Coordenadas = coordenadas
        self.Pertenece = pertenece
        self.Lista_Ciudades = []