
from ClaseCalefactor import calefactor

class electrico(calefactor):
    __potenciaMaxima : int

    def __init__(
        self, marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion, potenciaMaxima
    ):
        super().__init__(marca, modelo, paisFabricante, precioLista, formaPago, cantCuotas, promocion)
        self.__potenciaMaxima = potenciaMaxima

    @property
    def getPotenciaMaxima(self):
        return self.__potenciaMaxima

