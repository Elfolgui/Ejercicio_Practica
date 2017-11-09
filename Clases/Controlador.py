from Clases import *
import os

class Controlador(object):

    @classmethod
    def Menu_Agregar_Barrio(cls, Ciu, prov):
        os.system("cls")
        print("Ingrese un Nombre para su Barrio")
        n = input()
        os.system("cls")
        print("Un codigo para el Barrio")
        c = input()
        os.system("cls")
        print("Primer Par de coordenadas")
        cor_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        os.system("cls")
        print("Ingrese la cantidad de poblacion")
        p = input()
        os.system("cls")
        print("Ingrese la Ciudad a la que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Barrio(n, c, (cor_1, cor_2), p, pertenece, prov)
        if respuesta is not False:
            print("Entre")
            Ciu.Lista_Barrios.append(respuesta)
        if respuesta is False:
            print("Agregue una Ciudad con ese nombre antes de poder agregar un Barrio")
            input()
            return True

    @classmethod
    def Agregar_Barrio(cls, nombre, codigo, coordenadas, poblacion, pertenece, prov):
        for city in prov.Lista_Ciudades:
            if city.Nombre == pertenece:
                barrio = Barrio(nombre, codigo, coordenadas, poblacion, pertenece)
                return barrio
            else:
                return False
        return False

    @classmethod
    def Agregar_Ciudad(cls, nombre, codigo, coordenadas, pertenece, pais):
        for prov in pais.Lista_Provincias:
            if prov.Nombre == pertenece:
                ciudad = Ciudad(nombre, codigo, coordenadas, pertenece)
                return ciudad
            else:
                return False
        return False

    @classmethod
    def Agregar_Provincia(cls, nombre, codigo, coordenadas, pertenece, con):
        for pais in con.Lista_Paises:
            if pais.Nombre == pertenece:
                provincia = Provincia(nombre, codigo, coordenadas, pertenece)
                return provincia
            else:
                return False
        return False

    @classmethod
    def Agregar_Pais(cls, nombre, codigo, coordenadas, pertenece, mundo):
        for continente in mundo.Lista_Continentes:
            if continente.Nombre == pertenece:
                pais = Pais(nombre, codigo, coordenadas, pertenece)
                return pais
            else:
                return False
        return False

    @classmethod
    def Agregar_Continente(cls, nombre, codigo, coordenadas, mundo):
        for continente in mundo.Lista_Continentes:
            if continente.Nombre != nombre:
                pass
            else:
                return False
        continente = Continente(nombre, codigo, coordenadas)
        return continente

    @classmethod
    def Mostrar_Barrios(cls, mundo):
        os.system("cls")
        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    for ciu in pro.Lista_Ciudades:
                        print("|" + ciu.Nombre + "|" + "\n")
                        for bar in ciu.Lista_Barrios:
                            print("|" + bar.Nombre + "|")
        print("\n" + "Presione enter para volver")
        input()