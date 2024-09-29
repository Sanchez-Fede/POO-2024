
import rich
from clasePublicacion import publicacion

class libroImpreso(publicacion):

    __nombreAutor : str
    __fechaEdicion : str
    __cantPagina : int

    def __init__(self, titulo : str, categoria : str, precioBase : float, nombreAutor : int, fechaEdicion : float, cantPagina : str):
        super().__init__(titulo, categoria, precioBase)
        self.__nombreAutor = nombreAutor
        self.__fechaEdicion = fechaEdicion
        self.__cantPagina = cantPagina

    # def __repr__(self):
    #     super().mostrarDatosPublicacion()
    #     return f'''Nombre Autor: {self.__nombreAutor} Fecha Edicion: {self.__fechaEdicion} Cantidad de Pagina: {self.__cantPagina}'''

    def __str__(self) -> str:
        return super().__str__() + f'''Nombre Autor: {self.__nombreAutor} Fecha Edicion: {self.__fechaEdicion} Cantidad de Pagina: {self.__cantPagina}'''

    def getNombreAutor(self):
        return self.__nombreAutor

    def getFechaEdicion(self):
        return self.__fechaEdicion

    def getCantPagina(self):
        return self.__cantPagina

    def importeLibroImpreso(self):
        precioBase = super().getPrecioBase()
        antiguedad = 2024 - int(self.__fechaEdicion)
        porcentajeAntiguedad = float((antiguedad*precioBase)/100)
        return (precioBase - porcentajeAntiguedad)

