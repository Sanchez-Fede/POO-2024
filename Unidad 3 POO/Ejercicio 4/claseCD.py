
from clasePublicacion import publicacion

class cd(publicacion):

    __tiempoReproduccion : str
    __nombreNarrador : str

    def __init__(self, titulo, categoria, precioBase, tiempoReproduccion : str, nombreNarrador : str):
        super().__init__(titulo, categoria, precioBase)
        self.__tiempoReproduccion = tiempoReproduccion
        self.__nombreNarrador = nombreNarrador

    def mostrarDatosCD(self)->None:
        super().mostrarDatosPublicacion()
        print(f'''Tiempo Reproduccion: {self.__tiempoReproduccion} minutos Nombre Narrador: {self.__nombreNarrador}''')

    def getTiempoReproduccion(self):
        return self.__tiempoReproduccion

    def getNombreNarrador(self):
        return self.__nombreNarrador

    def importeCD(self):
        precioBase = super().getPrecioBase()
        porcentaje10 = float((10*precioBase)/100)
        return (precioBase + porcentaje10)