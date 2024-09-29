
#importo Nodo
#importo clase del objeto 

class listaEnlazada:

    __comienzo : any    #cambiar any por la Nodo
    __actual : any
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
            self.__inice = 0
            raise StopIteration
        else:
            self.__inice += 1
            dato = self.__actual.getPublicacion()
            self.__actual = self.__actual.getNodoSiguiente()
            return dato

    #def agregarNodo(self, unaPublicacion: publicacion):
    #      unNodo = Nodo(objeto)
    #      unNodo.setNodoSiguiente(self.__comienzo)
    #      self.__comienzo = unNodo
    #      self.__actual = unNodo
    #      self.__tope += 1

# Procesamiento:
