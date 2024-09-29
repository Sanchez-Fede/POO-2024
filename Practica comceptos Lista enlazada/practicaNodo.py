

class Nodo:
    # objeto va ser de la clase deseada
    __numero : int 
    __nodoSiguiente : object

    def __init__(self, objetoNum : object):
        self.__numero = objetoNum
        self.__nodoSiguiente = None

    def getNodoSiguiente(self):
        return self.__nodoSiguiente

    def setNodoSiguiente(self, objeto):
        self.__nodoSiguiente = objeto

    def getNumero(self):
        return self.__numero
