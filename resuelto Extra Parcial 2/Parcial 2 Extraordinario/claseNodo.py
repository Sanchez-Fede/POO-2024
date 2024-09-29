
from claseAnuncio import anuncio

class Nodo:
    __anuncio : anuncio  
    __nodoSiguiente : object

    def __init__(self, unAnuncio : anuncio):
        self.__anuncio = unAnuncio
        self.__nodoSiguiente = None #no cambia

    def getNodoSiguiente(self):
        return self.__nodoSiguiente

    def setNodoSiguiente(self, unNodo):
        self.__nodoSiguiente = unNodo

    def getAnuncio(self)->anuncio:
        return self.__anuncio
