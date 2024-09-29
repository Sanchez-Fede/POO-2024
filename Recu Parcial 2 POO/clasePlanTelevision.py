
from clasePlanes import planes

class planTelevision(planes):

    __cantCanalesNacionales : int
    __cantCanalesInternacionales : int

    def __init__(self,  nomCompañia, duracion, cobertura, precioBase, cantCanalesNacionales : int, cantCanalesInternacionales : int):
        super().__init__(nomCompañia, duracion, cobertura, precioBase)
        self.__cantCanalesNacionales = cantCanalesNacionales
        self.__cantCanalesInternacionales = cantCanalesInternacionales

    def __str__(self):
        return super().__str__() + f'''cantCanalesNacionales: {self.__cantCanalesNacionales} cantCanalesInternacionales: {self.__cantCanalesInternacionales}'''

    def getCantCanalesNacionales(self):
        return self.__cantCanalesNacionales

    def getCantCanalesInternacionales(self):
        return self.__cantCanalesInternacionales

    def calcularImporteTotal(self):
        if isinstance(self, planTelevision):
            if self.getCantCanalesInternacionales() > 10:
                porcetaje = self.calcularPorcentaje(15)
                importeCanalesInternacional = self.getPrecioBase() + porcetaje
                return importeCanalesInternacional
            else:
                return self.getPrecioBase()