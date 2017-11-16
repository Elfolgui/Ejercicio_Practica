from . import *
import os

class Controlador(object):

    @classmethod
    def Menu(cls):
        os.system("cls")
        print("1: Agregar Lugar")
        print("2: Modificar Lugar")
        print("3: Poblaciones")
        print("4: Mostrar Mundo")
        print("0: Salir" + "\n")

        selector = input()

        return selector

    @classmethod
    def Menu_Agregar(cls):
        os.system("cls")
        print("1: Agregar Barrio")
        print("2: Agregar Ciudad")
        print("3: Agregar Provincias")
        print("4: Agregar Pais")
        print("5: Agregar Continente" + "\n")

        selector = input()

        return selector

    @classmethod
    def Menu_Modificar(cls):
        os.system("cls")
        print("1: Modificar Barrio")
        print("2: Modificar Ciudad")
        print("3: Modificar Provincias")
        print("4: Modificar Pais")
        print("5: Modificar Continente" + "\n")

        selector = input()

        return selector

    @classmethod
    def Menu_Poblaciones(cls):
        os.system("cls")
        print("1: Paises")
        print("5: Continentes" + "\n")

        selector = input()

        return selector

    @classmethod
    def Poblacion_Pais(cls):
        os.system("cls")
        print("1: Mayor Poblacion")
        print("5: Menor Poblacion" + "\n")

        selector = input()

        return selector

    @classmethod
    def Poblacion_Continente(cls):
        os.system("cls")
        print("1: Mayor Poblacion")
        print("5: Menor Poblacion" + "\n")

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
    def Modificar_Barrio(cls, mundo):
        print("Ingre el Codigo del Barrio a modificar")
        Codigo_Barrio = input()
        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    for ciu in pro.Lista_Ciudades:
                        for bar in ciu.Lista_Barrios:
                            if bar.Codigo == int(Codigo_Barrio):
                                print("Barrio encontrado" + "\n" + "Indique lo que desee modificar")
                                respuesta = input()
                                if respuesta == "nombre":
                                    print("Ingrese el nuevo Nombre")
                                    Nombre = input()
                                    bar.Nombre = Nombre
                                elif respuesta == "poblacion":
                                    print("Ingrese el nuevo numero de poblacion")
                                    poblacion = input()
                                    bar.Poblacion = poblacion
                                elif respuesta == "coordenadas":
                                    print("Primer Punto")
                                    cor1 = input()
                                    cor1_1 = input()
                                    print("Segundo Punto")
                                    cor2 = input()
                                    cor2_2 = input()
                                    bar.Coordendas = ((cor1, cor1_1), (cor2, cor2_2))
                                elif respuesta == "borrar":
                                    ciu.Lista_Barrios.remove(bar)
                                print("Dato cambiado" + "\n" + "Aprete Enter para continuar")
                                input()
                                return

    @classmethod
    def Modificar_Ciudad(cls, mundo):
        print("Ingre el Codigo de la Ciudad a modificar")
        Codigo_Ciudad = input()
        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    for ciu in pro.Lista_Ciudades:
                        if ciu.Codigo == int(Codigo_Ciudad):
                            print("Ciudad encontrada" + "\n" + "Ingrese el nombre del atributo a modificar")
                            respuesta = input()
                            if respuesta == "nombre":
                                print("Ingrese el nuevo Nombre")
                                Nombre = input()
                                ciu.Nombre = Nombre
                            elif respuesta == "coordenadas":
                                print("Primer Punto")
                                cor1 = input()
                                cor1_1 = input()
                                print("Segundo Punto")
                                cor2 = input()
                                cor2_2 = input()
                                ciu.Coordendas = ((cor1, cor1_1), (cor2, cor2_2))
                            elif respuesta == "borrar":
                                for barrio in ciu.Lista_Barrios:
                                    ciu.Lista_Barrios.remove(barrio)
                                pro.Lista_Ciudades.remove(ciu)
                            print("Dato cambiado" + "\n" + "Aprete Enter para continuar")
                            input()
                            return

    @classmethod
    def Modificar_Provincia(cls, mundo):
        os.system("cls")
        print("Ingre el Codigo de la Provincia a modificar")
        Codigo_Provincia = input()
        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                for pro in pa.Lista_Provincias:
                    if pro.Codigo == int(Codigo_Provincia):
                        os.system("cls")
                        print("Provincia encontrada" + "\n" + "Ingrese el nombre del atributo a modificar")
                        respuesta = input()
                        if respuesta == "nombre":
                            print("Ingrese el nuevo Nombre")
                            Nombre = input()
                            pro.Nombre = Nombre
                        elif respuesta == "coordenadas":
                            print("Primer Punto")
                            cor1 = input()
                            cor1_1 = input()
                            print("Segundo Punto")
                            cor2 = input()
                            cor2_2 = input()
                            pro.Coordendas = ((cor1, cor1_1), (cor2, cor2_2))
                        elif respuesta == "borrar":
                            for ciudad in pro.Lista_Ciudades:
                                for barrio in ciudad.Lista_Barrios:
                                    ciudad.Lista_Barrios.remove(barrio)
                                pro.Lista_Ciudades.remove(ciudad)
                            pa.Lista_Provincias.remove(pro)
                        os.system("cls")
                        print("Dato cambiado o eliminado" + "\n" + "Aprete Enter para continuar")
                        input()

    @classmethod
    def Modificar_Pais(cls, mundo):
        os.system("cls")
        print("Ingre el Codigo del Pais a modificar")
        Codigo_Pais = input()
        for con in mundo.Lista_Continentes:
            for pa in con.Lista_Paises:
                if pa.Codigo == int(Codigo_Pais):
                    os.system("cls")
                    print("Pais encontrado" + "\n" + "Ingrese el nombre del atributo a modificar")
                    respuesta = input()
                    if respuesta == "nombre":
                        print("Ingrese el nuevo Nombre")
                        Nombre = input()
                        pa.Nombre = Nombre
                    elif respuesta == "coordenadas":
                        print("Primer Punto")
                        cor1 = input()
                        cor1_1 = input()
                        print("Segundo Punto")
                        cor2 = input()
                        cor2_2 = input()
                        pa.Coordendas = ((cor1, cor1_1), (cor2, cor2_2))
                    elif respuesta == "borrar":
                        for provincia in pa.Lista_Provincias:
                            for ciudad in provincia.Lista_Ciudades:
                                for barrio in ciudad.Lista_Barrios:
                                    ciudad.Lista_Barrios.remove(barrio)
                                provincia.Lista_Ciudades.remove(ciudad)
                            pa.Lista_Provincias.remove(provincia)
                        con.Lista_Paises.remove(pa)
                    os.system("cls")
                    print("Dato cambiado" + "\n" + "Aprete Enter para continuar")
                    input()
                    return

    @classmethod
    def Modificar_Continente(cls, mundo):
        os.system("cls")
        print("Ingre el Codigo del Continente a modificar")
        Codigo_Continente = input()
        for con in mundo.Lista_Continentes:
            if con.Codigo == int(Codigo_Continente):
                os.system("cls")
                print("Continente encontrado" + "\n" + "Ingrese el nombre del atributo a modificar")
                respuesta = input()
                if respuesta == "nombre":
                    print("Ingrese el nuevo Nombre")
                    Nombre = input()
                    con.Nombre = Nombre
                elif respuesta == "coordenadas":
                    print("Primer Punto")
                    cor1 = input()
                    cor1_1 = input()
                    print("Segundo Punto")
                    cor2 = input()
                    cor2_2 = input()
                    con.Coordendas = ((cor1, cor1_1), (cor2, cor2_2))
                elif respuesta == "borrar":
                    for pais in con.Lista_Paises:
                        for provincia in pais.Lista_Provincias:
                            for ciudad in provincia.Lista_Ciudades:
                                for barrio in ciudad.Lista_Barrios:
                                    ciudad.Lista_Barrios.remove(barrio)
                                provincia.Lista_Ciudades.remove(ciudad)
                            pais.Lista_Provincias.remove(provincia)
                        con.Lista_Paises.remove(pais)
                    mundo.Lista_Continentes.remove(con)
                os.system("cls")
                print("Dato cambiado" + "\n" + "Aprete Enter para continuar")
                input()
                return

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

    @classmethod
    def Mostrar_Pais_Mayor(cls, mundo):
        print("Ingrese un Codigo de un continente"+"\n")

        Codigo = input()

        for Con in mundo.Lista_Continentes:
            if Con.Codigo == Codigo:
                return Con.mayorPoblacion()

    @classmethod
    def Mostrar_Pais_Menor(cls, mundo):
        print("Ingrese un Codigo de un continente" + "\n")

        Codigo = input()

        for Con in mundo.Lista_Continentes:
            if Con.Codigo == Codigo:
                return Con.menorPoblacion()

    @classmethod
    def Mostrar_Continente_Mayor(cls, mundo):
        return mundo.mayorPoblacion()

    @classmethod
    def Mostrar_Continente_Menor(cls, mundo):
        return mundo.menorPoblacion()
