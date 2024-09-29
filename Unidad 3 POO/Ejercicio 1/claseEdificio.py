
from typing import List
from claseDepartamento import Departamento

class Edificio:

    __id : int
    __nombre : str
    __direccion : str
    __nombreEmpresa : str
    __cantPisos : int
    __cantDepartamentos : int
    __ListaDepartamento : list[Departamento]

    def __init__(self, id : int, nombre : str, direccion : str, nombreEmpresa : str, cantPisos : int, cantDepartamentos : int):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombreEmpresa = nombreEmpresa
        self.__cantPisos = cantPisos
        self.__cantDepartamentos = cantDepartamentos
        self.__ListaDepartamento = list()

    def add_Departamento(self, unDepartamento : Departamento):
            self.__ListaDepartamento.append(unDepartamento)

    def getListaDepartamento(self):
        return self.__ListaDepartamento

    def __rich__(self):
        return f'''
        ID: {self.__id} \t Nombre: {self.__nombre} \n Direccion: {self.__direccion} Empresa: {self.__nombreEmpresa} \n
        Cantidad de Pisos: {self.__cantPisos} \n Cantidad de Departamentos: {self.__cantDepartamentos}
        '''

    def mostrarPropietarios(self):
        for departamento in self.__ListaDepartamento:
            print(f"Propietario: {self.__ListaDepartamento.getPropietario()}")


    def getID(self):
        return self.__id


    def getNombre(self):
        return self.__nombre


    def getDirecion(self):
        return self.__direccion


    def getNombreEmpresa(self):
        return self.__nombreEmpresa


    def getCantidadPisos(self):
        return self.__cantPisos


    def getCantidadDepartamentos(self):
        return self.__cantDepartamentos
