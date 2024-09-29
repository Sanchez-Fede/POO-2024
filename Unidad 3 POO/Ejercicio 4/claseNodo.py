
from clasePublicacion import publicacion

class Nodo:
    __publicacion : publicacion
    __NodoSiguiente : object

    def __init__(self, unaPublicacion : publicacion):
        self.__publicacion = unaPublicacion
        self.__NodoSiguiente = None

    def setNodoSiguiente(self, unNodo):
        self.__NodoSiguiente = unNodo

    def getNodoSiguiente(self):
        return self.__NodoSiguiente

    def getPublicacion(self)->publicacion:
        return self.__publicacion