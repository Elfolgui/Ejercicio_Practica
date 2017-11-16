from .Clase_Base import *

class Continente(Clase_Base):

    def __init__(self, nombre, codigo, coordenadas):
        Clase_Base.__init__(self, nombre, codigo)
        self.Coordenadas = coordenadas
        self.Lista_Paises = []

    def mayorPoblacion(self):
        Mayor_Poblacion = 0
        Cantidad = 0
        for pais in self.Lista_Paises:
            for prov in pais.Lista_Provincias:
                for ciu in prov.Lista_Ciudades:
                    for bar in ciu.Lista_Barrios:
                        Cantidad += bar.Poblacion
            if Cantidad > Mayor_Poblacion:
                Mayor_Poblacion = Cantidad
        return Mayor_Poblacion

    def menorPoblacion(self):
        Menor_Poblacion = 1000000000000000
        Cantidad = 0
        for pais in self.Lista_Paises:
            for prov in pais.Lista_Provincias:
                for ciu in prov.Lista_Ciudades:
                    for bar in ciu.Lista_Barrios:
                        Cantidad += bar.Poblacion
            if Cantidad < Menor_Poblacion:
                Menor_Poblacion = Cantidad
        return Menor_Poblacion