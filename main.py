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
        selec = Controlador.Menu_Poblaciones()

        if selec == "1":
            sel = Controlador.Poblacion_Pais()

            if sel == "1":
                print("El Pais con mas poblacion tiene: " + Controlador.Mostrar_Pais_Mayor(Mundi) + " personas")
            if sel == "2":
                print("El Pais con menos poblacion tiene: " + Controlador.Mostrar_Pais_Menor(Mundi)+ " personas")

        if selec == "2":
            sel = Controlador.Poblacion_Continente()

            if sel == "1":
                print("El Continente con mas poblacion tiene: " + Controlador.Mostrar_Continente_Mayor(Mundi) + " personas")
            if sel == "2":
                print("El Continente con menos poblacion tiene: " + Controlador.Mostrar_Continente_Menor(Mundi) + " personas")

    if seleccionador == "4":
        Controlador.Mostrar_Mundo(Mundi)

    if seleccionador == "0":
        break