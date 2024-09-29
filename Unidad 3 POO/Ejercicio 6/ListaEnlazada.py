
from Nodo import Nodo
from claseElectrico import electrico
from claseA_Gas import a_gas

class listaEnlazada:

    __comienzo : Nodo
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
            self.__inice = 0
            raise StopIteration
        else:
            self.__inice += 1
            dato = self.__actual.getcale()
            self.__actual = self.__actual.getNodoSiguiente()
            return dato

    def agregarNodo(self, unCalefactor):
        unNodo = Nodo(unCalefactor)
        unNodo.setNodoSiguiente(self.__comienzo)
        self.__comienzo = unNodo
        self.__actual = unNodo
        self.__tope += 1

# Procesamiento
    def ingresarCalefactor(self):

        rtaUser = input(" Que tipo de Calefactor es? \n [ 1 ]: A gas \n [ 2 ]: Electrico")
        print("Ingrese datos del Calefactor:")

        if rtaUser == '1':
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            paisFabricante = input("Pais Fabricante: ")
            precioLista = float(input("Precio Lista: "))
            formaPago = input("Forma de Pago: ")
            cantCuotas = int(input("Cantidad de Cuotas: "))
            promocion = input("Promocion: ")
            matricula = input("Matricula: ")
            calorias = input("Calorias: ")

            calefactorGas = a_gas(marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion, matricula, calorias)
            self.agregarNodo(calefactorGas)

        elif rtaUser == '2':
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            paisFabricante = input("Pais Fabricante: ")
            precioLista = float(input("Precio Lista: "))
            formaPago = input("Forma de Pago: ")
            cantCuotas = int(input("Cantidad de Cuotas: "))
            promocion = input("Promocion: ")
            potenciaMaxima = int(input("Potencia Maxima: "))

            calefactorElectrico = electrico(marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion, potenciaMaxima)
            self.agregarNodo(calefactorElectrico)

    def buscarPosicionNodo(self, unaPosicion):
        nodoAux = Nodo()

    def ingresar_enPosicion(self):
        print("Desde la posicion 0 hasta {}".format(self.__tope))
        posicion = int(input("Teclee la posicion: "))

        if posicion < self.__tope:
            pass
        else:
            print("Valor incorrecto")