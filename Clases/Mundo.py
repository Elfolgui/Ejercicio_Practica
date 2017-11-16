
class Mundo(object):

    def __init__(self):
        self.Lista_Continentes = []

    def mayorPoblacion(self):
        Mayor_Poblacion = 0
        Cantidad = 0
        for con in self.Lista_Continentes:
            for pais in con.Lista_Paises:
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
        for con in self.Lista_Continentes:
            for pais in con.Lista_Paises:
                for prov in pais.Lista_Provincias:
                    for ciu in prov.Lista_Ciudades:
                        for bar in ciu.Lista_Barrios:
                            Cantidad += bar.Poblacion
            if Cantidad < Menor_Poblacion:
                Menor_Poblacion = Cantidad
        return Menor_Poblacion