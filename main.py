from Clases import *
import os

Con = Continente("Con", 747, ((0, 0),(100, 100)))

Bar = Barrio("Bar", 202, ((20, 20), (30, 30)), 30000, "Ciu")

Ciu = Ciudad("Ciu", 123, ((30, 30), (40, 40)), "Prov")

Prov = Provincia("Prov", 654, ((40, 40), (50, 50)), "Pa")

Pa = Pais("Pa", 951, ((50, 50),(60, 60)), "Con")

while True:
    print("1: Agregar Barrio")
    print("2: Agregar Ciudad")
    print("3: Agregar Provincias")
    print("4: Agregar Pais")
    print("5: Agregar Continente")

    selector = input()

    if selector == "1":
        Controlador.Menu_Agregar_Barrio(Ciu)
    if selector == "2":
        Controlador.Agregar_Ciudad()
    if selector == "3":
        Controlador.Agregar_Provincia()
    if selector == "4":
        Controlador.Agregar_Pais()
    if selector == "5":
        Controlador.Agregar_Continente()