from .Continente import *

class Barrio(Clase_Base):

    def __init__(self,  nombre, codigo, coordenadas, poblacion, pertenece):
        Clase_Base.__init__(self, nombre, codigo)
        self.Coordenadas = coordenadas
        self.Poblacion = poblacion
        self.Pertenece = pertenece
