
from clasePlanes import planes

class Nodo:
    __plan : planes
    __NodoSiguiente : object

    def __init__(self, unPlan : planes):
        self.__plan = unPlan
        self.__NodoSiguiente = None

    def setNodoSiguiente(self, unNodo):
        self.__NodoSiguiente = unNodo

    def getNodoSiguiente(self):
        return self.__NodoSiguiente

    def getPlan(self)->planes:
        return self.__plan