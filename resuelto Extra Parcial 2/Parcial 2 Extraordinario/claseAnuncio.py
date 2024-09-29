
import rich
import abc
from abc import ABC

class anuncio(ABC):

    __titulo : str
    __duracion : int
    __fechaCreacion : str
    __costoxSegundo : float
    __formato : str

    def __init__(self, titulo, duracion,  fechaCracion, costoSeg, formato):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__fechaCreacion = fechaCracion
        self.__costoxSegundo = costoSeg
        self.__formato = formato

    def __str__(self):
        return f'''Titulo: {self.__titulo} Duracion: {self.__duracion} \n Fecha Creacion: {self.__fechaCreacion} Costo por Segundo: {self.__costoxSegundo} \n Formato: {self.__formato}'''

    def getTitulo(self):
        return self.__titulo

    def getDuracion(self):
        return self.__duracion

    def getFechaCreacion(self):
        return self.__fechaCreacion

    def getCostoSegundo(self):
        return self.__costoxSegundo

    def getFormato(self):
        return self.__formato

    def calcularPorcentaje(self, unPorcentaje ):
        float(unPorcentaje)
        porcentaje = (self.__costoxSegundo * unPorcentaje) / 100
        return porcentaje

    @abc.abstractmethod
    def calcularImporteTotal(self):
        costoSegunDuracion = self.__costoxSegundo * self.__duracion
        return costoSegunDuracion