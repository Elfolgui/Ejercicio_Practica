from Clases import *
import os

Con = Continente("Con", 747, ((0, 0), (100, 100)))

Bar = Barrio("Bar", 202, ((20, 20), (30, 30)), 30000, "Ciu")

Ciu = Ciudad("Ciu", 123, ((30, 30), (40, 40)), "Prov")

Prov = Provincia("Prov", 654, ((40, 40), (50, 50)), "Pa")

Pa = Pais("Pa", 951, ((50, 50),(60, 60)), "Con")

Mundi = Mundo()

Ciu.Lista_Barrios.append(Bar)
Prov.Lista_Ciudades.append(Ciu)
Pa.Lista_Provincias.append(Prov)
Con.Lista_Paises.append(Pa)
Mundi.Lista_Continentes.append(Con)


while True:
    os.system("cls")
    print("1: Agregar Barrio")
    print("2: Agregar Ciudad")
    print("3: Agregar Provincias")
    print("4: Agregar Pais")
    print("5: Agregar Continente")
    print("6: Mostrar Barrios")
    print("7: Mostrar Ciudades")
    print("8: Mostrar Provincias")
    print("9: Mostrar Paises")
    print("10: Mostrar Continentes")
    print("0: Salir")

    selector = input()

    if selector == "1":
        if Controlador.Menu_Agregar_Barrio(Ciu, Prov):
            pass
    if selector == "2":
        Controlador.Agregar_Ciudad()
    if selector == "3":
        Controlador.Agregar_Provincia()
    if selector == "4":
        Controlador.Agregar_Pais()
    if selector == "5":
        Controlador.Agregar_Continente()
    if selector == "6":
        Controlador.Mostrar_Barrios(Mundi)
    if selector == "0":
        break