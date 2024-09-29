
import csv
import rich
from typing import List
from claseEdificio import Edificio
from claseDepartamento import Departamento

class gestorEdificio:
    __listaEdificios = list[Edificio]
    def __init__(self):
        self.__listaEdificios = list()

    def extraerEdificioCSV(self):
        with open("EdificioNorte.csv", 'r', newline='') as ArchivoEdificio:
            contenido = csv.reader(ArchivoEdificio, delimiter = ';')

            for fila in contenido:
                if len(fila) == 6:
                    suID = int(fila[0])
                    nombre = fila[1]
                    direccion = fila[2]
                    nombreEmpresa = fila[3]
                    cantPisos = int(fila[4])
                    cantDepartamentos = int(fila[5])
                    unEdificio = Edificio(suID, nombre, direccion, nombreEmpresa, cantPisos, cantDepartamentos)
                    self.__listaEdificios.append(unEdificio)
            
                elif len(fila) == 7:
                    suID = int(fila[0])
                    propietario = fila[1]
                    numPiso = int(fila[2])
                    numDepartamento = int(fila[3])
                    cantHabitaciones = int(fila[4])
                    cantBaños = int(fila[5])
                    superficieCubierta = float(fila[6].replace(';', '.'))
                    unDepartamento = Departamento(suID, propietario, numPiso, numDepartamento, cantHabitaciones, cantBaños, superficieCubierta)
                    self.__listaEdificios[-1].agregarDepartamento(unDepartamento)

    def mostrarListaEdificios(self):
        for edificio in self.__listaEdificios:
            rich.print(edificio)

    def buscarPropietario(self, nombreEdificio : str) -> int:
        i = 0
        tam = len(self.__listaEdificios)
        while i < tam and self.__listaEdificios[i].getNombre() != nombreEdificio:
            i += 1

        if i < tam:
            self.mostrarPropietario(self.__listaEdificios[i].getListaDepartamento())
        else:
            print("No se encuentra")

    def mostrarPropietario(self, unaLista : Departamento):
        # Tercera version
        for departamento in unaLista:
            print(f"Propietario: {unaLista.getPropietario()}")

    def mostrarSupTotal(self, unNombre:str ):
        tam = len(self.__listaEdificios)
        posicion = self.buscarEdificio(unNombre)

        if posicion < tam:
            self.__listaEdificios[posicion].getCantidadDepartamentos() * self.__listaEdificios[posicion]