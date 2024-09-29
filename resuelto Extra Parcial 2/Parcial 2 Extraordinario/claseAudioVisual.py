
from claseAnuncio import anuncio

class audioVisual(anuncio):

    __resolucionVideo : int

    def __init__(self, titulo, duracion,  fechaCracion, costoSeg, formato, resolucionVideo):
        super().__init__(titulo, duracion,  fechaCracion, costoSeg, formato)
        self.__resolucionVideo = resolucionVideo

    def __str__(self):
        return super().__str__() + f'''Resolucion Video: {self.__resolucionVideo}'''

    def getResolucionVideo(self):
        return self.__resolucionVideo

    def calcularImporteTotal(self):
        if isinstance(self, audioVisual):
            if self.getResolucionVideo() == 1440:
                porcentaje = self.calcularPorcentaje(1.5)
                costoTotoal = self.getCostoSegundo() * self.getDuracion() + porcentaje
                return costoTotoal
            elif self.getResolucionVideo() == 1080:
                porcentaje = self.calcularPorcentaje(1)
                costoTotoal = self.getCostoSegundo() * self.getDuracion() + porcentaje
                return costoTotoal
            elif self.getResolucionVideo() != 1440 or 1080:
                costoTotoal = self.getCostoSegundo() * self.getDuracion()
                return costoTotoal