
import abc 
from abc import ABC

class planes(ABC):

    __nombreCompañia : str
    __duracionPlan : str
    __coberturaGeografica : str
    __precioBase : float

    def __init__(self, nombreCompañia : str, duracionPlan : str,  coberturaGeografica : str, precioBase : float):
        self.__nombreCompañia = nombreCompañia
        self.__duracionPlan = duracionPlan
        self.__coberturaGeografica = coberturaGeografica
        self.__precioBase = precioBase

    def __str__(self)->str:
        return f'''nombreCompañia: {self.__nombreCompañia} duracionPlan: {self.__duracionPlan} coberturaGeografica: {self.__coberturaGeografica} precioBase: {self.__precioBase}'''

    def getNombreCompañia(self):
        return self.__nombreCompañia

    def getDuracionPlan(self):
        return self.__duracionPlan

    def getCoberturaGeografica(self):
        return self.__coberturaGeografica

    def getPrecioBase(self):
        return self.__precioBase

    def calcularPorcentaje(self, unPorcentaje ):
        float(unPorcentaje)
        porcentaje = (self.__precioBase * unPorcentaje) / 100
        return porcentaje

    @abc.abstractmethod
    def calcularImporteTotal(self):
        pass