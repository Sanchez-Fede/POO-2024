
from practicaNodo import Nodo

class listaEnlazada:

    __comienzo : Nodo    #cambiar any por la Nodo
    __actual : Nodo
    __indice : int
    __tope : int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.__inice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__inice += 1
            dato = self.__actual.getNumero()
            self.__actual = self.__actual.getNodoSiguiente()
            return dato

# Agregar por la cabeza de la lista:
    def agregarNodo(self, unNumero):
        unNodo = Nodo(unNumero)
        unNodo.setNodoSiguiente(self.__comienzo)
        self.__comienzo = unNodo
        self.__actual = unNodo
        self.__indice += 1
        self.__tope += 1

# Procesamiento:

    def insertarFinal(self, unNumero):
        #Funciona
        nuevoNodo = Nodo(unNumero)
        if self.__comienzo == None:
            self.__comienzo = Nodo(unNumero)
        else:
            nodoAux = self.__comienzo
            while nodoAux.getNodoSiguiente() != None:
                nodoAux = nodoAux.getNodoSiguiente()
            nodoAux.setNodoSiguiente(nuevoNodo)

    def mostrarLista(self):
        #Funiona
        nodoAux = self.__comienzo
        while nodoAux != None:
            dato = nodoAux.getNumero()
            print("Numero: ", dato)
            nodoAux = nodoAux.getNodoSiguiente()

    def buscarNumero(self, Numero):
        #Funciona
        nodoAux = self.__comienzo
        while nodoAux != None and nodoAux.getNumero() != Numero:
            nodoAux = nodoAux.getNodoSiguiente()

        if nodoAux != None:
            print("Si se encontro el numero :) ")
        else:
            print("No se encontro")