
class publicacion:

    __titulo : str
    __categoria : str
    __precioBase : float

    def __init__(self, titulo : str, categoria : str, precioBase : float):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precioBase = precioBase

    # def __repr__(self):
    #     return f'''Nombre: A: {self.__titulo} B: {self.__categoria} C: {self.__precioBase}'''

    # def mostrarDatosPublicacion(self)->None:
    #     print(f'''Nombre: {self.__titulo} Categoria: {self.__categoria} Precio Base: {self.__precioBase}''')

    def __str__(self) -> str:
        return f'''Nombre: {self.__titulo} Categoria: {self.__categoria} Precio Base: {self.__precioBase}\n'''

    def getTitulo(self):
        return self.__titulo

    def getCategoria(self):
        return self.__categoria

    def getPrecioBase(self):
        return self.__precioBase