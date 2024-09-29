
from abc import ABC, abstractmethod
class calefactor(ABC):

    __marca : str
    __modelo : str
    __paisFabricante : str
    __precioLista : float
    __formaPago : str
    __cantCuotas : int
    __promocion : str

    def __init__(self, marca : str, modelo : str,  paisFabricante : str, precioLista : float, formaPago : str, cantCuotas : int, promocion : str):
        self.__marca = marca
        self.__modelo = modelo
        self.__paisFabricante = paisFabricante
        self.__precioLista = precioLista
        self.__formaPago = formaPago
        self.__cantCuotas = cantCuotas
        self.__promocion = promocion

    @property
    def __repr__(self):
        return f'''marca: {self.__marca} modelo: {self.__modelo} paisFabricante: {self.__paisFabricante} \n Precio Lista: {self.__precioLista} Forma Pago: {self.__formaPago} cantidad Cuotas: {self.__cantCuotas} Promocion: {self.__promocion}'''

    @property
    def getMarca(self):
        return self.__marca

    @property
    def getModelo(self):
        return self.__modelo

    @property
    def getPaisFabricante(self):
        return self.__paisFabricante

    @property
    def getPrecioLista(self):
        return self.__precioLista

    @property
    def getFormaPago(self):
        return self.__formaPago

    @property
    def getCantCuotas(self):
        return self.__cantCuotas

