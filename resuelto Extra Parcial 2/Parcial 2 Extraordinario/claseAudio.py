
from claseAnuncio import anuncio

class audio(anuncio):

    __canalAudio : str

    def __init__(self, titulo, duracion,  fechaCracion, costoSeg, formato, canalAudio):
        super().__init__(titulo, duracion,  fechaCracion, costoSeg, formato)
        self.__canalAudio = canalAudio

    def __str__(self):
        return super().__str__() + f'''Canal de Audio: {self.__canalAudio}'''

    def getCanalAudio(self):
        return self.__canalAudio

    def calcularImporteTotal(self):
        if isinstance(self, audio):
            if self.getCanalAudio() == 'surround':
                porcentaje = self.calcularPorcentaje(0.5)
                costoTotoal = self.getCostoSegundo() * self.getDuracion() + porcentaje
                return costoTotoal
            elif self.getCanalAudio() == 'mono':
                porcentaje = self.calcularPorcentaje(0.1)
                costoTotoal = self.getCostoSegundo() * self.getDuracion() + porcentaje
                return costoTotoal