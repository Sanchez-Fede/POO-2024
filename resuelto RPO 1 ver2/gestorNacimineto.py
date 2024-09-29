
import csv
import rich
from typing import List
from claseNacimiento import nacimiento

class gestorNacimiento:
    __ListaNacimiento : List[nacimiento]

    def __init__(self):
        self.__ListaNacimiento = list()

# Funciones ================================== #
    def extraerDatosCSV(self):
        with open("Nacimientos.csv", 'r', newline='') as archivoNacimientos:
            contenido = csv.reader(archivoNacimientos, delimiter = ';')
            archivoNacimientos.__next__()
            for fila in contenido:
                dniMadre = int(fila[0])
                tipoParto = fila[1]
                fecha = fila[2]
                hora = fila[3]
                peso = float(fila[4].replace(",", "."))
                altura = float(fila[5])
                unNacimiento = nacimiento(dniMadre, tipoParto, fecha, hora, peso, altura)
                self.__ListaNacimiento.append(unNacimiento)
        print("Carga completa de Nacimientos....")

    def mostrarDatosBebes(self):
        for unBebe in self.__ListaNacimiento:
            rich.print(unBebe)

#item a
    def buscarPartoBebe(self, unDni)->str:
        i = 0
        cant = len(self.__ListaNacimiento)
        while i < cant and unDni != self.__ListaNacimiento[i].getDniMadre(): 
            i += 1
        
        if i < cant:
            tipoParto = self.__ListaNacimiento[i].getTipoParto()
            return tipoParto

    def mostrarHijos(self, unDni):
        for unBebe in self.__ListaNacimiento:
            if unDni == unBebe.getDniMadre():
                print(f''' Peso : {unBebe.getPeso()}    Altura : {unBebe.getAltura()} ''')

#item b
    def ordenarPorDNI(self):
        self.__ListaNacimiento.sort()
        print("Ordenamiento completo....")
        #Funciona bien el ordenamiento.

    def contadorNacimientos(self, unDni : int):
        contBebes = 0
        for unNacimiento in self.__ListaNacimiento:
            if unDni == unNacimiento.getDniMadre():
                contBebes += 1
        return contBebes

