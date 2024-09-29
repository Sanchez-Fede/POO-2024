
class Ladrillo:

    __alto : int
    __largo : int
    __ancho : int
    __cantidad : int
    __id : int
    __kgMateriaUtilizada : float
    __costo : float

    def __init__(
            self, alto : int, largo : int, ancho : int,
            cantidad : int , id : int, kgMaterial_Utilizado : float, costo : float
    ):
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__cantidad = cantidad
        self.__id = id
        self.__kgMateriaUtilizada = kgMaterial_Utilizado
        self.__costo = costo

    def getAlto(self):
        return self.__alto
    
    def getLargo(self):
        return self.__largo
    
    def getAncho(self):
        return self.__ancho
    
    def getCantidad(self):
        return self.__cantidad
    
    def getID(self):
        return self.__id
    
    def getkgMaterialUtilizada(self):
        return self.__kgMateriaUtilizada
    
    def getCosto(self):
        return self.__costo
