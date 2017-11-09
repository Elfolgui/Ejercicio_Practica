from Clases import *
import os

class Controlador(object):

    @classmethod
    def Menu_Agregar_Barrio(cls, Ciu):
        os.system("cls")
        print("Ingrese un Nombre")
        n = input()
        os.system("cls")
        print("Ingrese un codigo")
        c = input()
        os.system("cls")
        print("Ingrese Primer Punto")
        cor_1 = input()
        os.system("cls")
        print("Ingrese Segundo Punto")
        cor_2 = input()
        os.system("cls")
        print("Ingrese la cantidad de poblacion")
        p = input()
        os.system("cls")
        print("Ingrese la Ciudad a la que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Barrio(n, c, (cor_1, cor_2), p, pertenece)
        if respuesta is not False:
            Ciu.Lista_Barrios.append(respuesta)

    @classmethod
    def Agregar_Barrio(cls, nombre, codigo, coordenadas, poblacion, pertenece):
        for city in Provincia.Lista_Ciudades:
            if city.Nombre == pertenece:
                barrio = Barrio(nombre, codigo, coordenadas, poblacion, pertenece)
                return barrio
            else:
                return False
        return False

    @classmethod
    def Agregar_Ciudad(cls, nombre, codigo, coordenadas, pertenece):
        for prov in Pais.Lista_Provincias:
            if prov.Nombre == pertenece:
                ciudad = Ciudad(nombre, codigo, coordenadas, pertenece)
                return ciudad
            else:
                return False
        return False

    @classmethod
    def Agregar_Provincia(cls, nombre, codigo, coordenadas, pertenece):
        for pais in Continente.Lista_Paises:
            if pais.Nombre == pertenece:
                provincia = Provincia(nombre, codigo, coordenadas, pertenece)
                return provincia
            else:
                return False
        return False

    @classmethod
    def Agregar_Pais(cls, nombre, codigo, coordenadas, pertenece):
        for continente in Mundo.Lista_Continentes:
            if continente.Nombre == pertenece:
                pais = Pais(nombre, codigo, coordenadas, pertenece)
                return pais
            else:
                return False
        return False

    @classmethod
    def Agregar_Continente(cls, nombre, codigo, coordenadas):
        for continente in Mundo.Lista_Continentes:
            if continente.Nombre != nombre:
                pass
            else:
                return False
        continente = Continente(nombre, codigo, coordenadas)
        return continente