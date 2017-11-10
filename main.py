from Clases import *

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
    seleccionador = Controlador.Menu()

    if seleccionador == "1":

        selector = Controlador.Menu_Agregar()

        if selector == "1":
            if Controlador.Menu_Agregar_Barrio(Ciu, Prov):
                pass
        if selector == "2":
            Controlador.Menu_Agregar_Ciudad(Prov, Pa)
        if selector == "3":
            Controlador.Menu_Agregar_Provincia(Con, Pa)
        if selector == "4":
            Controlador.Menu_Agregar_Pais(Con, Mundi)
        if selector == "5":
            Controlador.Menu_Agregar_Continente(Mundi)
        if selector == "0":
            break

    if seleccionador == "2":

        selector = Controlador.Menu_Modificar()

        if selector == "1":
            if Controlador.Modificar_Barrio(Mundi):
                pass
        if selector == "2":
            Controlador.Modificar_Ciudad(Mundi)
        if selector == "3":
            Controlador.Modificar_Provincia(Mundi)
        if selector == "4":
            Controlador.Modificar_Pais(Mundi)
        if selector == "5":
            Controlador.Modificar_Continente(Mundi)
        if selector == "0":
            break

    if seleccionador == "3":
        Controlador.Mostrar_Mundo(Mundi)

    if seleccionador == "0":
        break