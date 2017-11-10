from . import *
import os

class Controlador(object):

    @classmethod
    def Menu(cls):
        os.system("cls")
        print("1: Agregar Barrio")
        print("2: Agregar Ciudad")
        print("3: Agregar Provincias")
        print("4: Agregar Pais")
        print("5: Agregar Continente")
        print("6: Mostrar Mundo")
        print("0: Salir" + "\n")

        selector = input()

        return selector

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
        cor_1_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        cor_2_2 = input()
        os.system("cls")
        print("Ingrese la cantidad de poblacion")
        p = input()
        os.system("cls")
        print("Ingrese la Ciudad a la que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Barrio(n, c, ((cor_1, cor_1_1), (cor_2, cor_2_2)), p, pertenece, prov, Ciu)
        if respuesta is not False:
            Ciu.Lista_Barrios.append(respuesta)
        if respuesta is False:
            print("Agregue una Ciudad con ese nombre o cambie el codigo de su barrio antes de poder agregarlo")
            input()
            return True

    @classmethod
    def Agregar_Barrio(cls, nombre, codigo, coordenadas, poblacion, pertenece, prov, ciu):
        for city in prov.Lista_Ciudades:
            if city.Nombre == pertenece:
                barrio = Barrio(nombre, codigo, coordenadas, poblacion, pertenece)
                for bar in ciu.Lista_Barrios:
                    if bar.Codigo == barrio.Codigo:
                        return False
                return barrio
        return False

    @classmethod
    def Menu_Agregar_Ciudad(cls, prov, Pais):
        os.system("cls")
        print("Ingrese un Nombre para su Ciudad")
        n = input()
        os.system("cls")
        print("Un codigo para la Ciudad")
        c = input()
        os.system("cls")
        print("Primer Par de coordenadas")
        cor_1 = input()
        cor_1_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        cor_2_2 = input()
        os.system("cls")
        print("Ingrese la Provincia a la que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Ciudad(n, c, ((cor_1, cor_1_1),(cor_2, cor_2_2)), pertenece, Pais, prov)
        if respuesta is not False:
            prov.Lista_Ciudades.append(respuesta)
        if respuesta is False:
            print("Agregue una Provincia con ese nombre o cambie el codigo de su Ciudad antes de poder agregarla")
            input()
            return True

    @classmethod
    def Agregar_Ciudad(cls, nombre, codigo, coordenadas, pertenece, pais, provincia):
        for prov in pais.Lista_Provincias:
            if prov.Nombre == pertenece:
                ciudad = Ciudad(nombre, codigo, coordenadas, pertenece)
                for ciu in provincia.Lista_Ciudades:
                    if ciu.Codigo == ciudad.Codigo:
                        return False
                return ciudad
        return False

    @classmethod
    def Menu_Agregar_Provincia(cls, Con, Pais):
        os.system("cls")
        print("Ingrese un Nombre para su Provincia")
        n = input()
        os.system("cls")
        print("Un codigo para la Provincia")
        c = input()
        os.system("cls")
        print("Primer Par de coordenadas")
        cor_1 = input()
        cor_1_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        cor_2_2 = input()
        os.system("cls")
        print("Ingrese la Ciudad a la que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Provincia(n, c, ((cor_1, cor_1_1), (cor_2, cor_2_2)), pertenece, Con, Pais)
        if respuesta is not False:
            Pais.Lista_Provincias.append(respuesta)
        if respuesta is False:
            print("Agregue una Ciudad con ese nombre o cambie el codigo de su Provincia antes de poder agregarla")
            input()
            return True

    @classmethod
    def Agregar_Provincia(cls, nombre, codigo, coordenadas, pertenece, con, Pais):
        for pais in con.Lista_Paises:
            if pais.Nombre == pertenece:
                provincia = Provincia(nombre, codigo, coordenadas, pertenece)
                for prov in Pais.Lista_Provincias:
                    if prov.Codigo == provincia.Codigo:
                        return False
                return provincia
        return False

    @classmethod
    def Menu_Agregar_Pais(cls, Con, Mundi):
        os.system("cls")
        print("Ingrese un Nombre para su Pais")
        n = input()
        os.system("cls")
        print("Un codigo para el Pais")
        c = input()
        os.system("cls")
        print("Primer Par de coordenadas")
        cor_1 = input()
        cor_1_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        cor_2_2 = input()
        os.system("cls")
        print("Ingrese el Continente al que pertenece")
        pertenece = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Pais(n, c, ((cor_1, cor_1_1), (cor_2, cor_2_2)), pertenece, Mundi, Con)
        if respuesta is not False:
            print("Entre")
            Con.Lista_Paises.append(respuesta)
        if respuesta is False:
            print("Agregue un Continente con ese nombre o cambie el codigo de su Pais antes de poder agregarlo")
            input()
            return True

    @classmethod
    def Agregar_Pais(cls, nombre, codigo, coordenadas, pertenece, mundo, con):
        print(pertenece)
        for continente in mundo.Lista_Continentes:
            if continente.Nombre == pertenece:
                pais = Pais(nombre, codigo, coordenadas, pertenece)
                for pa in con.Lista_Paises:
                    if pa.Codigo == pais.Codigo:
                        print("SoyIgual")
                        return False
                print("devuelvo pais")
                return pais
        return False

    @classmethod
    def Menu_Agregar_Continente(cls, Mundi):
        os.system("cls")
        print("Ingrese un Nombre para su Continente")
        n = input()
        os.system("cls")
        print("Un codigo para el Continente")
        c = input()
        os.system("cls")
        print("Primer Par de coordenadas")
        cor_1 = input()
        cor_1_1 = input()
        os.system("cls")
        print("Segundo Par de coordenadas")
        cor_2 = input()
        cor_2_2 = input()
        os.system("cls")
        respuesta = Controlador.Agregar_Continente(n, c, ((cor_1, cor_1_1), (cor_2, cor_2_2)), Mundi)
        if respuesta is not False:
            Mundi.Lista_Continentes.append(respuesta)
        if respuesta is False:
            print("Cambie el codigo de su Continente antes de poder agregarlo")
            input()
            return True

    @classmethod
    def Agregar_Continente(cls, nombre, codigo, coordenadas, mundo):
        for continente in mundo.Lista_Continentes:
            if continente.Nombre != nombre:
                pass
            else:
                return False
        conti = Continente(nombre, codigo, coordenadas)
        for continente in mundo.Lista_Continentes:
            if continente.Codigo == conti.Codigo:
                return False
        return conti

    @classmethod
    def Mostrar_Mundo(cls, mundo):
        os.system("cls")
        for con in mundo.Lista_Continentes:
            print("|" + con.Nombre + "|")

        print("\n")

        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                print("|" + pa.Nombre + "|" + "\n")
            print("  ")

        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    print("|" + pro.Nombre + "|" + "\n")
                print("  ")

        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    for ciu in pro.Lista_Ciudades:
                        print("|" + ciu.Nombre + "|" + "\n")
                    print("  ")

        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    for ciu in pro.Lista_Ciudades:
                        for bar in ciu.Lista_Barrios:
                            print("|" + bar.Nombre + "|")
                        print("  ")
        print("\n" + "Presione enter para volver")
        input()