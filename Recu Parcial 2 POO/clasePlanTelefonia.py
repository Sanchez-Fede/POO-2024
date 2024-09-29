
from clasePlanes import planes

class planTelefonia(planes):

    __tipoLLamada : str
    __cantMinutos : int

    def __init__(self, nomCompañia, duracion, cobertura, precioBase, tipoLLamada : str, cantMinutos : int):
        super().__init__(nomCompañia, duracion, cobertura, precioBase)
        self.__tipoLLamada = tipoLLamada
        self.__cantMinutos = cantMinutos

    def __str__(self):
        return super().__str__() +  f'''tipoLLamada: {self.__tipoLLamada} cantMinutos: {self.__cantMinutos}'''

    def getTipoLLamada(self):
        return self.__tipoLLamada

    def getCantMinutos(self):
        return self.__cantMinutos

    def calcularImporteTotal(self):
        if isinstance(self, planTelefonia):
            if self.getTipoLLamada() == 'internacional':
                porcentaje = self.calcularPorcentaje(20)
                importeInternacional = self.getPrecioBase() + porcentaje
                return importeInternacional
            elif self.getTipoLLamada() == 'locales':
                porcentaje = self.calcularPorcentaje(7.5)
                importeLocal = self.getPrecioBase() - porcentaje
                return importeLocal
            elif self.getTipoLLamada() == 'larga distancia':
                importeLargaDistancia = self.getPrecioBase()
                return importeLargaDistancia

    # def calcularImporteTotal(self):
    #     if self.getTipoLLamada() == 'Internacional':
    #         importeInternacional = float(self.getPrecioBase() * 0.5)
    #         return importeInternacional
    #     elif self.getTipoLLamada() == 'Local':
    #         importeLocal = float((self.getPrecioBase() - (self.getPrecioBase() - 0.075)))
    #         return importeLocal
    #     elif self.getTipoLLamada() == 'Larga Distancia':
    #         importeLargaDistancia = float(self.getPrecioBase())
    #         return importeLargaDistancia
