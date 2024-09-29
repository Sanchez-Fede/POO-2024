
from ClaseCalefactor import calefactor

class a_gas:

    __matricula : str
    __calorias : int

    def __init__(self, marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion , matricula : str, calorias : int):
        super().__init__(marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion)
        self.__matricula = matricula
        self.__calorias = calorias

    def __repr__(self):
        return f'''matricula: {self.__matricula} calorias: {self.__calorias}'''

    @property
    def getMatricula(self):
        return self.__matricula

    @property
    def getCalorias(self):
        return self.__calorias