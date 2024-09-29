
from ClaseCalefactor import calefactor

class Nodo:

    __calefactor : calefactor
    __nodoSiguiente : object

    def __init__(self, unCalefactor : calefactor):
        self.__calefactor = unCalefactor
        self.__nodoSiguiente = None

    def getNodoSiguiente(self):
        return self.__nodoSiguiente

    def setNodoSiguiente(self, unCalefactor):
        self.__nodoSiguiente = unCalefactor

    def getObjeto(self):
        return self.__objecto
