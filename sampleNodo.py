
# importar clase del objecto
class Nodo:
    # objeto va ser de la clase deseada
    objecto : object 
    __nodoSiguiente : object

    def __init__(self, objeto : object):
        self.__objecto = objeto
        self.__nodoSiguiente = None

    def getNodoSiguiente(self):
        return self.__nodoSiguiente

    def setNodoSiguiente(self, objeto):
        self.__nodoSiguiente = objeto

    def getObjeto(self):
        return self.__objecto
